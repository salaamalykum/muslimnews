---
license: mit
language:
- zh
size_categories:
- n<1K
task_categories:
- text-retrieval
- question-answering
- text-generation
- summarization
pretty_name: "MuslimNews: Global Islamic & International News RAG Corpus"
tags:
- islamic-studies
- muslim-news
- international-news
- rag
- chinese-nlp
- knowledge-base
- llms-txt
- croissant
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---

# MuslimNews: Global Islamic & International News RAG Corpus (v1.0.0) 🌍🕌

**MuslimNews** is a rigorously curated, zero-noise Chinese corpus containing **173 verified international news articles** and **1092 semantic RAG chunks** covering global Muslim communities, Middle East & South Asia public policy, religious heritage protection, Halal economy, and cross-cultural dialogues.

Synchronized directly from [`https://salaamalykum.com/cn/topic/国际新闻`](https://salaamalykum.com/cn/topic/%E5%9B%BD%E9%99%85%E6%96%B0%E9%97%BB), this dataset follows a strict **Dual-Track Publishing Architecture**:
- **Human-Readable Portal & Markdown Archive**: Hosted on GitHub ([`salaamalykum/muslimnews`](https://github.com/salaamalykum/muslimnews)) and GitHub Pages ([`https://salaamalykum.github.io/muslimnews/`](https://salaamalykum.github.io/muslimnews/)).
- **Machine-Trainable Views**: Hosted here on Hugging Face (`qurancn/muslimnews`) in page-indexed **Apache Parquet** (`data/*.parquet`) for instant Dataset Viewer / DuckDB SQL querying, alongside derived **RAG Chunks**, **Alpaca SFT**, and **ShareGPT** JSONL views in `sft/`.

> [!TIP]
> **Human Readers:** Looking for the full text with all images rendered natively? Navigate to **[Files and versions -> content](https://huggingface.co/datasets/qurancn/muslimnews/tree/main/content)** or visit our **[GitHub Pages Portal](https://salaamalykum.github.io/muslimnews/)**!

---

## Dataset Views & Format Integrity

To uphold strict data quality standards, we separate the **Primary Document RAG View** from **Derived SFT Views**:

1. **Primary Document RAG View (`default` Parquet config in `data/*.parquet` & `sft/muslimnews_dataset.jsonl`)**:
   - Contains the complete, unmanipulated 173 news articles with SHA-256 content hashes, original URLs, canonical URLs, authors, ISO-8601 timestamps, and topic tags.
2. **Semantic Sliding-Window RAG Chunks (`sft/muslimnews_rag_chunks.jsonl`)**:
   - 1092 overlapping semantic chunks (`chunk_id`, `article_id`, `title`, `text`, `original_url`, `content_hash`) engineered for hybrid BM25 + Dense Vector Retrieval and cross-corpus alignment with `quran_rag_dataset`.
3. **Instruction-Tuning Views (`sft/muslimnews_alpaca.jsonl` & `sft/muslimnews_sharegpt.jsonl`)**:
   - Explicitly structured single-turn (`instruction` / `input` / `output`) and multi-turn (`conversations` array) records derived from each article's editorial lead (`【导读与核心背景】`), summary (`【核心内容概要】`), and full report body.

### Data Schema (`default` Parquet Config)

| Field | Type | Description |
|---|---|---|
| `id` | `string` | Original WeCenter article ID from `salaamalykum.com`. |
| `slug` | `string` | URL-safe deterministic identifier (`{id}_{sanitized_title}`). |
| `title` | `string` | Headline of the international news article. |
| `summary` | `string` | Clean 220-character editorial lead summary. |
| `text` | `string` | Full zero-noise GitHub Flavored Markdown body. |
| `original_url` | `string` | Source URL (`https://salaamalykum.com/cn/article/{id}`). |
| `canonical_url` | `string` | GitHub Pages canonical URL. |
| `author` | `string` | Original contributor username. |
| `pub_date` | `string` | ISO-8601 publication timestamp (UTC). |
| `updated_at` | `string` | Synchronized batch release timestamp (`2026-10-30T07:50:00Z`). |
| `language` | `string` | BCP-47 language tag (`zh-CN`). |
| `tags` | `string` | Comma-separated topic tags mapped from `aws_topic`. |
| `content_hash` | `string` | SHA-256 cryptographic digest of `text`. |
| `word_count` | `int64` | Character length of `text`. |
| `preview_excerpt` | `string` | 150-character snippet for rapid UI & Embedding Atlas rendering. |

---

## Quickstart Usage

```python
from datasets import load_dataset

# Load the primary RAG document corpus
ds = load_dataset("qurancn/muslimnews", split="train")
print(ds[0]["title"], ds[0]["original_url"])
```

## Citation

```bibtex
@dataset{muslimnews_rag_2026,
  author       = {Salaamalykum Open Data Hub},
  title        = {MuslimNews: A Curated RAG Corpus of 173 International News Articles on the Global Muslim World},
  month        = oct,
  year         = 2026,
  publisher    = {Hugging Face & GitHub},
  version      = {v1.0.0},
  url          = {https://github.com/salaamalykum/muslimnews}
}
```
