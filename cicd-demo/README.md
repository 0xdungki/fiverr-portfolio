# GitHub Actions CI/CD Pipeline Demo

Professional CI/CD setup with automated testing, building, and deployment.

## Features

✅ **Automated Testing** - Runs tests on every push/PR
✅ **Code Quality** - Linting with flake8
✅ **Code Coverage** - Coverage reports with Codecov
✅ **Docker Build** - Automated Docker image building
✅ **Multi-Environment Deploy** - Staging + Production
✅ **Health Checks** - Post-deployment verification
✅ **Notifications** - Slack integration

## Pipeline Stages

### 1. Test
- Checkout code
- Install dependencies (with caching)
- Run linter (flake8)
- Run tests with coverage
- Upload coverage reports

### 2. Build
- Build Docker image
- Push to Docker Hub
- Tag with commit SHA + latest

### 3. Deploy
- **Staging** (develop branch)
  - Deploy to staging server
  - Run migrations
  - Health check
  
- **Production** (main branch)
  - Deploy to production server
  - Run migrations
  - Health check
  - Slack notification

## Setup Instructions

### 1. Required Secrets

Add these secrets to your GitHub repository:

```
DOCKER_USERNAME
DOCKER_PASSWORD
STAGING_HOST
STAGING_USER
STAGING_SSH_KEY
PROD_HOST
PROD_USER
PROD_SSH_KEY
SLACK_WEBHOOK (optional)
```

### 2. Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   └── your_code.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

### 3. Workflow Triggers

- **Push to main** → Test + Build + Deploy to Production
- **Push to develop** → Test + Build + Deploy to Staging
- **Pull Request** → Test only

## Example Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

## Benefits

- **Fast feedback** - Know if your code breaks within minutes
- **Consistent deployments** - Same process every time
- **Zero downtime** - Rolling deployments with health checks
- **Rollback ready** - Tagged images for easy rollback
- **Team visibility** - Everyone sees build status

## Customization

Easily customize for:
- Different languages (Node.js, Go, Ruby, etc.)
- Different platforms (AWS, Heroku, DigitalOcean)
- Different testing frameworks
- Additional stages (security scanning, performance tests)

---

**Need a custom CI/CD pipeline?** Contact me on Fiverr: @dungki_dev

**Typical delivery:** 2-3 days for complete setup
