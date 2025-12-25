#!/usr/bin/env python3
"""
Test the fixed Stripe Connect functionality with HTTPS URLs
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

def test_account_link_with_https():
    print("🔗 Testing account link creation with HTTPS URLs...")
    
    try:
        import stripe
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
        
        # Create a test Express account first
        account = stripe.Account.create(
            type='express',
            country='US',
            email='test@example.com',
            capabilities={
                'card_payments': {'requested': True},
                'transfers': {'requested': True},
            },
            business_type='individual',
        )
        
        print(f"✅ Created test account: {account.id}")
        
        # Create account link with HTTPS URLs
        account_link = stripe.AccountLink.create(
            account=account.id,
            refresh_url="https://localhost:3000/settings?refresh=true",
            return_url="https://localhost:3000/settings?success=true",
            type="account_onboarding",
        )
        
        print(f"✅ Created account link successfully!")
        print(f"   URL: {account_link.url}")
        print(f"   Expires at: {account_link.expires_at}")
        
        # Clean up
        try:
            stripe.Account.delete(account.id)
            print(f"✅ Cleaned up test account")
        except:
            pass
            
        return True
        
    except Exception as e:
        print(f"❌ Account link creation failed: {e}")
        return False

def main():
    print("🚀 TESTING STRIPE CONNECT FIX")
    print("=" * 50)
    
    stripe_key = os.getenv('STRIPE_SECRET_KEY', '')
    if stripe_key.startswith('sk_live_'):
        print("⚠️  Using LIVE Stripe keys - HTTPS URLs required")
    elif stripe_key.startswith('sk_test_'):
        print("✅ Using TEST Stripe keys - HTTP URLs allowed")
    else:
        print("❌ No valid Stripe key found")
        return
    
    if test_account_link_with_https():
        print("\n✅ Stripe Connect should now work!")
        print("\n📋 RECOMMENDATIONS:")
        print("1. For development: Use test keys (sk_test_...)")
        print("2. For production: Ensure your app runs on HTTPS")
        print("3. Update your frontend URLs to use HTTPS in production")
    else:
        print("\n❌ Still having issues. Check the error message above.")

if __name__ == "__main__":
    main()
