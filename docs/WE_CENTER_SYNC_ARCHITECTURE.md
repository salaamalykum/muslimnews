# WeCenter 3.1.9 (OpenResty + PHP 7.0 + MySQL) Automated Dual-Track Publishing & 2026 GEO Architecture

## 1. System Overview

This document specifies the production-grade synchronization pipeline connecting the **WeCenter 3.1.9** community engine (`https://salaamalykum.com/cn/topic/%E5%9B%BD%E9%99%85%E6%96%B0%E9%97%BB`) running on **OpenResty + PHP 7.0 + MySQL** with our dual-track public AI knowledge infrastructure:
1. **GitHub Human-Readable & GEO Portal**: [`https://github.com/salaamalykum/muslimnews`](https://github.com/salaamalykum/muslimnews) & [`https://salaamalykum.github.io/muslimnews/`](https://salaamalykum.github.io/muslimnews/)
2. **Hugging Face Machine-Trainable Hub**: [`https://huggingface.co/datasets/qurancn/muslimnews`](https://huggingface.co/datasets/qurancn/muslimnews)

## 2. WeCenter 3.1.9 Database & Hook Architecture

In WeCenter 3.1.9 (`WecenterDoc.md`), articles published under Topic `国际新闻` (`topic_id = 636`) are stored across three core relational tables:
- `aws_article`: Stores `id`, `uid`, `title`, `message` (BBCode/HTML), `add_time`, `views`, `comments`.
- `aws_topic`: Stores `topic_id`, `topic_title`, `topic_description`.
- `aws_topic_relation`: Maps `topic_id = 636` to `item_id` (`aws_article.id`) where `type = 'article'`.

### Production Hook Integration (`system/models/muslimnews_sync.php`)
- Drop `metadata/wecenter_sync_plugin.php` into `models/muslimnews_sync.php`.
- In `app/publish/ajax.php` (`publish_article_action`), invoke:
  ```php
  $this->model('muslimnews_sync')->dispatch_github_sync($payload);
  ```
- **Security Hardening (OpenResty + PHP-FPM 7.0)**:
  - Credentials (`WECENTER_GITHUB_PAT`) are injected exclusively via `/etc/php/7.0/fpm/pool.d/www.conf` (`env[WECENTER_GITHUB_PAT] = ...`) with `chmod 0600` root-only permissions.
  - OpenResty WAF blocks any external access to `/system/` or `.sql`/`.env` paths.

## 3. 2026 Next-Gen AI Crawler & GEO (Generative Engine Optimization) Stack

To maximize crawl frequency and citation density across **OAI-SearchBot / GPTBot (OpenAI)**, **ClaudeBot (Anthropic)**, **Google-Extended (Gemini)**, **PerplexityBot**, and **GrokBot (xAI)**, this repository implements five complementary machine-discovery protocols:
1. **`llms.txt` & `llms-full.txt` + `.well-known/llms.txt`**: Deterministic Markdown index and single-shot full-corpus context payload (`173` articles) for zero-hop LLM ingestion.
2. **MLCommons Croissant 1.0 (`metadata/croissant.json`)**: Standardized JSON-LD dataset descriptor natively parsed by Google Dataset Search, Hugging Face, and frontier AI training pipelines.
3. **Page-Indexed Apache Parquet (`row_group_size=1024`, `write_page_index=True`)**: Enables zero-copy HTTP Range request scanning by Hugging Face DuckDB and remote AI agents without downloading full archives.
4. **Triple-Synchronized Timestamps (`2026-10-30T07:50:00Z`, `v1.0.0`)**: Synchronizes `_config.yml`, `sitemap.xml`, `feed.xml` (RSS 2.0), `atom.xml` (Atom 1.0), and GitHub Release tags to trigger high-priority delta re-indexing.
5. **Dual-View Schema.org JSON-LD (`Dataset` + `NewsArticle`)**: Every GitHub Pages HTML view embeds structured JSON-LD linking `sameAs` back to the canonical WeCenter URL (`https://salaamalykum.com/cn/article/{id}`) and Hugging Face Parquet shards.
