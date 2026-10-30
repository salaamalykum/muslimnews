# Contributing to MuslimNews RAG Corpus

We welcome contributions from researchers, journalists, and AI engineers working on multilingual Islamic and international news retrieval.

## Quality Gate Requirements for Pull Requests
1. **Normalized Markdown (`content/`)**: Every article must include all required YAML frontmatter fields (`article_id`, `title`, `original_url`, `canonical_url`, `author`, `pub_date`, `updated_at`, `lastmod`, `language`, `topics`, `content_hash`).
2. **Cryptographic Verification**: `content_hash` must match the exact SHA-256 hex digest of the normalized Markdown body.
3. **Triple Timestamp Synchronization**: Any batch update must simultaneously update `_config.yml`, `sitemap.xml`, `feed.xml`, `atom.xml`, and `CHANGELOG.md`.
4. **Zero Credential Policy**: Never commit API tokens, passwords, or private keys.
