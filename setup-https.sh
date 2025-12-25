#!/bin/bash
# Setup HTTPS for local development with mkcert

echo "🔒 Setting up HTTPS for local development..."

# Check if mkcert is installed
if ! command -v mkcert &> /dev/null; then
    echo "Installing mkcert..."
    
    # Install mkcert based on OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64"
        chmod +x mkcert-v*-linux-amd64
        sudo mv mkcert-v*-linux-amd64 /usr/local/bin/mkcert
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install mkcert
    else
        echo "❌ Unsupported OS. Please install mkcert manually."
        exit 1
    fi
fi

# Create local CA
mkcert -install

# Create certificates for localhost
mkdir -p certs
cd certs
mkcert localhost 127.0.0.1 ::1

echo "✅ HTTPS certificates created in ./certs/"
echo ""
echo "📋 Next steps:"
echo "1. Update your docker-compose.yml to use HTTPS"
echo "2. Configure nginx or your web server to use the certificates"
echo "3. Access your app via https://localhost instead of http://localhost"
