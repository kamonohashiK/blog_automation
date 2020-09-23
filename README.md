# blog_automation
Githubに上げたIssueを元にブログを書けないかどうかの実験

## Usage
.envファイルを作成し、以下の内容を記載。

- GITHUB_ID: Githubのアカウント名
- REPOSITORY_NAME: Issue等を取ってくる対象のリポジトリ名
- HATENA_ID: はてなID
- BLOG_URL: 投稿先のブログのドメイン
- HATENA_PASSWORD: はてなブログAtomPubのAPIキー

AtomPubのAPIキーははてなブログの「設定」＞「詳細設定」と進んでAtomPubの項目で確認可能。
認証にはBASIC認証を用いているが、httpsから始まるドメインのブログでないと利用できないらしいので注意。