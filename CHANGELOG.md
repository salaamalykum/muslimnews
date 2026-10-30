# Changelog

All notable changes to the **MuslimNews** corpus are documented in this file.

## [v1.0.0] - 2026-10-30 (2026-10-30T07:50:00Z)
### Added
- **173 Normalized Markdown Articles (`content/`)**: Full 1:1 extraction from `https://salaamalykum.com/cn/topic/%E5%9B%BD%E9%99%85%E6%96%B0%E9%97%BB` (Topic ID `636`: `国际新闻`) with `original_url`, `canonical_url`, `author`, `pub_date`, `updated_at`, `language`, `topics`, and SHA-256 `content_hash`.
- **Dual-Track Machine Views (`metadata/` & Hugging Face `qurancn/muslimnews`)**:
  - `muslimnews_dataset.jsonl` (173 document records)
  - `muslimnews_rag_chunks.jsonl` (1092 sliding-window semantic chunks aligned with `quran_rag_dataset`)
  - `muslimnews_alpaca.jsonl` & `muslimnews_sharegpt.jsonl` (verified SFT views)
  - `croissant.json` (MLCommons Croissant 1.0 JSON-LD metadata)
  - Page-indexed Apache Parquet splits (`train`, `validation`, `test`) on Hugging Face.
- **10-Language README Suite**: Full documentation in English, Simplified Chinese, Spanish, Standard Arabic, Hindi, French, Indonesian, Bengali, Portuguese, and Urdu.
- **GitHub Pages Portal & 2026 AI Crawler GEO Suite**: `index.html`, `llms.txt`, `llms-full.txt`, `sitemap.xml`, `feed.xml`, `atom.xml`, `robots.txt`, and WeCenter 3.1.9 PHP 7.0 sync plugin (`metadata/wecenter_sync_plugin.php`).
