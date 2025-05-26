# Rate Limiting Security Improvements

This document outlines the rate limiting security improvements implemented to address Issue #6 in the CSEC_322_FINAL_PROJECT repository.

## Overview

Rate limiting is a crucial security measure that helps protect applications from various attacks, including:
- Brute force attacks on authentication endpoints
- Denial of Service (DoS) attacks
- Credential stuffing attacks
- Resource exhaustion

## Changes Implemented

### 1. Stricter Rate Limits for Sensitive Endpoints

| Endpoint | Previous Limit | New Limit | Reason |
|----------|---------------|-----------|--------|
| Login (`/login`) | 10 per minute | 5 per minute | Lower threshold to better protect against brute force attacks |
| Password Reset Request (`/reset_password_request`) | 5 per hour | 3 per 15 minutes | More restrictive sliding window to balance security and usability |
| Password Reset with Token (`/reset_password/<token>`) | 5 per hour | 3 per 15 minutes | Consistent with password reset request endpoint |

### 2. Enhanced Rate Limiter Configuration

- Changed rate limiting strategy from `fixed-window` to `moving-window` for more accurate rate limiting
- Enabled rate limit headers to provide client applications with visibility into remaining requests
- Configured standardized header names for better integration with security tools
- Disabled error swallowing to ensure rate limit violations are properly handled

### 3. Improved Error Handling for Rate Limit Violations

- Added mandatory delay (1 second) when rate limits are exceeded to slow down automated attacks
- Implemented logging of all rate limit violations for security monitoring
- Differentiated error responses based on endpoint sensitivity:
  - Minimal information for sensitive endpoints (login, password reset)
  - Standard responses for other endpoints
  - JSON responses for API endpoints

### 4. Testing Capability

Created a test script (`test_rate_limits.py`) to validate rate limiting functionality:
- Tests login endpoint rate limiting
- Tests password reset request endpoint rate limiting
- Tests password reset token endpoint rate limiting
- Provides detailed logging and results summary

## Security Benefits

These improvements provide the following security benefits:

1. **Reduced Vulnerability to Brute Force Attacks**: Stricter limits on authentication endpoints make password guessing attacks significantly more difficult
2. **Better Protection Against DoS**: More accurate rate limiting with the moving-window strategy prevents resource exhaustion
3. **Enhanced Security Visibility**: Logging of rate limit violations helps identify potential attacks
4. **Improved User Experience**: Clear error messages for legitimate users who hit rate limits
5. **Security Testing Capability**: Ability to validate rate limiting effectiveness with the test script

## Best Practices Implemented

1. Rate limits tailored to endpoint sensitivity (stricter for authentication)
2. Moving-window strategy for accurate rate limiting
3. Standardized rate limit headers for client visibility
4. Minimal information disclosure in error responses
5. Security event logging

## Usage Guidelines

### Running Rate Limit Tests

To validate the rate limiting functionality:

```
python test_rate_limits.py
```

You can also specify a custom base URL:

```
python test_rate_limits.py --url http://your-app-url
```

### Expected Results

When the application is properly configured, the tests should report:
- Rate limit exceeded (429) responses after multiple rapid requests
- Appropriate headers indicating the rate limit status
- Consistent behavior across all sensitive endpoints
