# Web Search Util - DuckDuckGo検索およびWebページ抽出用ユーティリティ

## 概要
`web-search-util` は、DuckDuckGoを利用したWeb検索およびWebページ内容抽出を行うためのPythonユーティリティです。  
このプロジェクトは、**APIサーバー機能**と**MCPサーバー機能**の両方を提供します。

---

## 機能一覧

### 🧩 API機能 (`src/web_search_util/api/api_server.py`)
`api_server.py` は、HTTP経由でWeb検索やページ抽出を行うAPIを提供します。

#### 主なエンドポイント
| エンドポイント | メソッド | 説明 |
|----------------|----------|------|
| `/search_wikipedia` | GET | Wikipediaで指定キーワードを検索（日本語対応） |
| `/ddgs_search` | GET | DuckDuckGoでWeb検索を実行 |
| `/extract_webpage` | GET | 指定URLのWebページからテキストとリンクを抽出 |
| `/download_file` | GET | 指定URLのファイルをダウンロード |

#### 起動方法
```bash
uv run -m web_search_util.api.api_server
```

---

### ⚙️ MCP機能 (`src/web_search_util/mcp/mcp_server.py`)
`mcp_server.py` は、ClineなどのMCP対応クライアントから利用可能なMCPサーバーを提供します。

#### 提供ツール
| ツール名 | 説明 |
|-----------|------|
| `search_wikipedia` | 日本語Wikipedia検索 |
| `ddgs_search` | DuckDuckGo検索 |
| `extract_webpage` | Webページ内容抽出 |
| `download_file` | ファイルダウンロード |

#### 起動方法
```bash
uv run -m web_search_util.mcp.mcp_server
```

---

## 前提条件
以下のソフトウェアがインストールされている必要があります：
- Visual Studio Code
- Cline
- Python 3.10+
- uv
- Microsoft Edge（Playwright経由で利用）

---

## セットアップ手順

1. リポジトリをクローンします。
    ```bash
    git clone https://github.com/knd3dayo/web-search-util.git
    cd web-search-util
    ```

2. Python仮想環境を作成します。
    ```bash
    python -m venv venv
    ```

3. 仮想環境を有効化し、依存関係をインストールします。
    ```bash
    venv\Scripts\activate
    pip install .
    ```

4. `sample_cline_mcp_settings.json` を参考に、`cline_mcp_settings.json` に設定を追加します。

    ```json
    "web_search_util": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "<PATH_TO_VENV>",
        "run",
        "-m",
        "web_search_util.mcp.mcp_server"
      ],
      "env": {
        "PLAYWRIGHT_HEADLESS": "false",
        "PLAYWRIGHT_BROWSER": "msedge"
      }
    }
    ```

5. ClineのMCPサーバー一覧に `web_search_util` が表示され、有効になっていれば設定完了です。

---

## 認証付きサイトの利用（任意）
認証が必要なサイトを扱う場合は、Playwrightでセッションを保存します。

```bash
venv\Scripts\activate
playwright codegen --channel=msedge --save-storage <PATH_TO_AUTH_JSON>
```

保存したJSONファイルを `PLAYWRIGHT_AUTH_JSON` 環境変数に設定してください。

---

## ライセンス
このプロジェクトは [MIT License](LICENSE) のもとで公開されています。
