#!/bin/bash

# Automated deployment script for OrthoMed Voice Bot
echo "🚀 Starting automated deployment..."

# Check if running on Railway
if [ ! -z "$RAILWAY_ENVIRONMENT" ]; then
    echo "✅ Detected Railway environment"
    export PORT=${PORT:-8080}
    gunicorn app:app --bind 0.0.0.0:$PORT
    exit 0
fi

# Check if running on Render
if [ ! -z "$RENDER" ]; then
    echo "✅ Detected Render environment"
    export PORT=${PORT:-10000}
    gunicorn app:app --bind 0.0.0.0:$PORT
    exit 0
fi

# Local development
echo "🔧 Running in development mode"
python app.py