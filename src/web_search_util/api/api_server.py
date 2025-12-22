from typing import Annotated, Any
from dotenv import load_dotenv
from pydantic import Field
from web_search_util.core.search_wikipedia_ja import search_wikipedia_ja
from web_search_util.core.web_util import WebUtil, WebSearchResult
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# Wikipedia検索ツールを登録
@router.get("/search_wikipedia")
def search_wikipedia(
    query: Annotated[str, Field(description="String to search for")], 
    lang: Annotated[str, Field(description="Language of Wikipedia")], 
    num_results: Annotated[int, Field(description="Maximum number of results to display")]
    ) -> Annotated[list[str], Field(description="List of related articles from Wikipedia")]:
    """
    This function searches Wikipedia with the specified keywords and returns related articles.
    """
    return search_wikipedia_ja(query, lang, num_results)

# duckduckgo_searchツールで検索した結果を返す
@router.get("/ddgs_search")
async def ddgs_search(
    query: Annotated[str, "The search query"],
    max_results: Annotated[int, "Maximum number of results to return"] = 10,
    site: Annotated[str, "Site to restrict the search to (optional)"] = "",
    detail: Annotated[bool, "If True, returns detailed results including the page content and a list of links from the result pages. Default is False"] = False
) -> Annotated[list[WebSearchResult], "List of search results from DuckDuckGo"]:
    return await WebUtil.ddgs_search(query, max_results, site, detail)
        
        
# 指定したURLのWebページからテキストとリンクを抽出するツールを登録
@router.get("/extract_webpage")
async def extract_webpage(
    url: Annotated[str, "URL of the web page to extract text and links from"]
) -> Annotated[dict[str, Any], "Dictionary containing 'output' (extracted text) and 'urls' (list of links with href and link text)"]:
    text, urls = await WebUtil.extract_webpage(url)
    result: dict[str, Any] = {}
    result["output"] = text
    result["urls"] = urls
    return result

# ファイルをダウンロードするツールを登録
@router.get("/download_file", response_model=bool)
def download_file(
    url: Annotated[str, "URL of the file to download"],
    save_path: Annotated[str, "Path to save the downloaded file"]
) -> Annotated[bool, "True if the file was downloaded successfully, False otherwise"]:
    return WebUtil.download_file(url, save_path)

app.include_router(router, prefix="/api/web_search_util")

if __name__ == "__main__":
    import uvicorn
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000)