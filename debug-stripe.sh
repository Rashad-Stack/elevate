#!/bin/bash
# Debug Stripe Connect Issues

echo "🔍 STRIPE CONNECT DEBUGGING CHECKLIST"
echo "=" * 60

echo "1. CHECK ENVIRONMENT VARIABLES:"
echo "   STRIPE_SECRET_KEY: ${STRIPE_SECRET_KEY:0:20}..."
echo "   STRIPE_PUBLISHABLE_KEY: ${STRIPE_PUBLISHABLE_KEY:0:20}..."
echo "   FRONTEND_URL: $FRONTEND_URL"

echo ""
echo "2. CHECK KEY TYPES:"
if [[ $STRIPE_SECRET_KEY == sk_live_* ]]; then
    echo "   ⚠️  Using LIVE keys - HTTPS required"
elif [[ $STRIPE_SECRET_KEY == sk_test_* ]]; then
    echo "   ✅ Using TEST keys - HTTP allowed"
else
    echo "   ❌ Invalid or missing Stripe key"
fi

echo ""
echo "3. COMMON ISSUES & SOLUTIONS:"
echo "   - 'HTTPS required' error → Use test keys or set up HTTPS"
echo "   - 'Invalid API Key' error → Check your Stripe dashboard for correct keys"
echo "   - 'Authentication required' error → Check user login status"
echo "   - 'Connect account not found' error → User needs to create account first"

echo ""
echo "4. TESTING STEPS:"
echo "   a) Test with curl:"
echo "      curl -X GET http://localhost:8000/api/stripe-connect/account/ \\"
echo "           -H 'Authorization: Bearer YOUR_JWT_TOKEN'"
echo ""
echo "   b) Check Django logs for detailed errors"
echo "   c) Use browser dev tools to see network requests"
echo "   d) Test the management command:"
echo "      python manage.py test_stripe_connect"

echo ""
echo "5. FRONTEND DEBUGGING:"
echo "   - Check browser console for JavaScript errors"
echo "   - Verify API client configuration"
echo "   - Check authentication token in requests"
echo "   - Ensure CORS is properly configured"
