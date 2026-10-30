# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| v1.0.x  | :white_check_mark: |

## Security Standards
- **Zero-Secret Repository**: All synchronization scripts use system keyring / environment variables (`WECENTER_GITHUB_PAT`, `HF_TOKEN`). No secrets are stored in code or git history.
- **Content Integrity**: All 173 articles are signed with SHA-256 `content_hash` digests to prevent poisoning during RAG ingestion.
- **Reporting a Vulnerability**: Contact `bropeace@protonmail.com` or open a security advisory on GitHub.
