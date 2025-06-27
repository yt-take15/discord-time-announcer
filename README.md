# discord-time-announcer

# Discord 時報ボット（discord-time-announcer）
このボットは、毎時10分ごとに指定したDiscordのボイスチャンネルに参加し、音声で時刻をお知らせするプログラムです

## 主な機能
毎10分ごと（00:00, 00:10, 00:20...）に音声で時刻をお知らせします(コメントアウトしている部分は一時間ごとです)
ボイスチャンネルに自動で参加・退室します
">ping", ">test"などのコマンドで正常に動作しているか確認できます

## 使用した言語・ライブラリ
Python 3.11
- [discord.py](https://github.com/Rapptz/discord.py)：Bot本体の機能
- FFmpeg：音声ファイルの再生に使用（`FFmpegPCMAudio`）
- python-dotenv：".env"ファイルからトークンやチャンネルIDを読み込む
- pytz：日本時間（JST）での時刻取得に使用

## 実行方法
1. このリポジトリをクローンまたはダウンロードします
2. ".env" ファイルをプロジェクト内に作成し、以下のように記入してください
  DISCORD_TOKEN=あなたのボットトークン
  VOICE_CHANNEL_ID=対象のボイスチャンネルID
3. "main.py"を実行
