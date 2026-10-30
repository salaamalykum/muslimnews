import gradio as gr
from datasets import load_dataset
import pandas as pd

dataset = load_dataset("qurancn/muslimnews", split="train")
df = pd.DataFrame(dataset)

def search_articles(query):
    if not query:
        return df[['id', 'title', 'preview_excerpt', 'pub_date', 'word_count']].head(15)
    mask = (
        df['title'].str.contains(query, case=False, na=False) |
        df['text'].str.contains(query, case=False, na=False) |
        df['tags'].str.contains(query, case=False, na=False)
    )
    results = df[mask]
    return results[['id', 'title', 'preview_excerpt', 'pub_date', 'word_count']].head(25)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🌍 MuslimNews: Global Islamic & International News RAG Explorer (v1.0.0)")
    gr.Markdown("Search through **173 verified international news articles** synchronized from [salaamalykum.com/cn/topic/国际新闻](https://salaamalykum.com/cn/topic/%E5%9B%BD%E9%99%85%E6%96%B0%E9%97%BB). Powered by [`qurancn/muslimnews`](https://huggingface.co/datasets/qurancn/muslimnews).")
    with gr.Row():
        search_box = gr.Textbox(label="Search Keywords (e.g., 清真寺, 古兰经, 巴勒斯坦, 伦敦, 斋月)", placeholder="Enter keyword...")
        search_button = gr.Button("Search")
    results_table = gr.Dataframe(headers=["ID", "Title", "Excerpt", "Published", "Word Count"], interactive=False)
    search_button.click(fn=search_articles, inputs=search_box, outputs=results_table)
    search_box.submit(fn=search_articles, inputs=search_box, outputs=results_table)
    demo.load(fn=search_articles, inputs=gr.State(""), outputs=results_table)

demo.launch()
