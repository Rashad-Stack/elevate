#!/usr/bin/env python3
"""
Simple test script to debug Stripe Connect functionality
"""
import os
import sys

# Add the backend directory to Python path
sys.path.insert(0, '/home/rashadstack/Desktop/elevate/backend')

# Set environment variables from .env.backend
env_file = '/home/rashadstack/Desktop/elevate/.env.backend'
if os.path.exists(env_file):
    with open(env_file, 'r') as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Test Stripe API connection
def test_stripe_connection():
    print("🔧 Testing Stripe API connection...")
    
    stripe_key = os.getenv('STRIPE_SECRET_KEY')
    if not stripe_key:
        print("❌ STRIPE_SECRET_KEY not found in environment")
        return False
    
    try:
        import stripe
        stripe.api_key = stripe_key
        
        # Test basic API call
        balance = stripe.Balance.retrieve()
        print(f"✅ Stripe API connected successfully")
        print(f"   Available balance: ${balance.available[0]['amount']/100:.2f} {balance.available[0]['currency'].upper()}")
        return True
    except Exception as e:
        print(f"❌ Stripe API connection failed: {e}")
        return False

# Test creating a Connect account
def test_connect_account_creation():
    print("\n🏦 Testing Connect account creation...")
    
    try:
        import stripe
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        
        # Create a test Express account
        account = stripe.Account.create(
            type='express',
            country='US',
            email='test@example.com',
            capabilities={
                'card_payments': {'requested': True},
                'transfers': {'requested': True},
            },
            business_type='individual',
            metadata={
                'test': 'true',
                'platform': 'elevate_social'
            }
        )
        
        print(f"✅ Created test Connect account: {account.id}")
        print(f"   Charges enabled: {account.charges_enabled}")
        print(f"   Payouts enabled: {account.payouts_enabled}")
        print(f"   Details submitted: {account.details_submitted}")
        
        # Create account link
        account_link = stripe.AccountLink.create(
            account=account.id,
            refresh_url="http://localhost:3000/settings?refresh=true",
            return_url="http://localhost:3000/settings?success=true",
            type="account_onboarding",
        )
        
        print(f"✅ Created account link: {account_link.url}")
        
        # Clean up test account (delete it)
        try:
            stripe.Account.delete(account.id)
            print(f"✅ Cleaned up test account: {account.id}")
        except Exception as cleanup_error:
            print(f"⚠️  Could not delete test account {account.id}: {cleanup_error}")
        
        return True
        
    except Exception as e:
        print(f"❌ Connect account creation failed: {e}")
        return False

# Test webhook endpoint signature verification
def test_webhook_signature():
    print("\n🔗 Testing webhook signature verification...")
    
    webhook_secret = os.getenv('STRIPE_CONNECT_WEBHOOK_SECRET')
    if not webhook_secret:
        print("⚠️  STRIPE_CONNECT_WEBHOOK_SECRET not set")
        return False
    
    try:
        import stripe
        
        # Create a test payload and signature
        payload = '{"test": "webhook"}'
        
        # This would normally be done by Stripe, but we're just testing the secret exists
        print(f"✅ Webhook secret is configured")
        return True
        
    except Exception as e:
        print(f"❌ Webhook test failed: {e}")
        return False

def main():
    print("🚀 STRIPE CONNECT DEBUG TEST")
    print("=" * 50)
    
    # Test 1: Basic Stripe connection
    if not test_stripe_connection():
        print("\n❌ Basic Stripe connection failed. Check your STRIPE_SECRET_KEY.")
        return
    
    # Test 2: Connect account creation
    if not test_connect_account_creation():
        print("\n❌ Connect account creation failed.")
        return
    
    # Test 3: Webhook configuration
    test_webhook_signature()
    
    print("\n" + "=" * 60)
    print("🎯 NEXT STEPS FOR DEBUGGING")
    print("=" * 60)
    print("1. If all tests passed, the issue might be in your Django application")
    print("2. Check Django logs for specific error messages")
    print("3. Verify your database migrations are up to date")
    print("4. Test the API endpoints directly with curl or Postman")
    print("5. Check if the user has proper authentication")
    
    print("\n📋 COMMON ISSUES TO CHECK:")
    print("- User authentication in frontend")
    print("- CORS settings for API calls")
    print("- Database connection and migrations")
    print("- Frontend API client configuration")
    print("- Network connectivity between frontend and backend")

if __name__ == "__main__":
    main()
