# README(no_poke20)

# 1.概要

---

## 1−1. 目的
---

### 実装目的

- 某配信者のファンサイトとして、ポケットモンスターシリーズ配信企画での使用を想定したアプリケーションを作成する
    - 企画の概要
        - ポケットモンスターシリーズ
        - ゲームを進めていく中で、初見のポケモンと遭遇した際、その姿を見ずに図鑑の説明文だけで絵を描いて似ていたら捕獲できるという
    - 課題
        - 検索エンジンから検索するとどうしてもポケモンの画像等ネタバレになる情報が表示されてしまう
        - 視聴者から図鑑情報のテキストのみを都度送付してもらっており、リスクも高く利便性も低い状況であった

### 実装概要

- ポケモンの名称を入力、ソフトを選択することで、図鑑説明分のみが検索できる機能を実装する
- ポケモンのイラストは表示させない（図鑑説明のみでポケモンを描くという企画のため）
- PCでの使用をメインのスコープとするが、ポートフォリオとして作成するため、スマホ対応のフレキシブルレイアウトも作成する
- UIは配信画面に表示させた際に他配信画面オブジェクトとの整合性が取れるよう、レトロゲーム調のデザインとする
- 図鑑データ収集用に、スクレイピングツールを作成する
- 実際に利用してもらう想定のため、ドメインの取得、およびSSL化は実施する

### その他、学習としての目的

- 前職で担当していたのがアプリケーション層のサーバーサイド機能実装、保守運用のみ
    - →他分野の知識が薄いことが個人的な課題であったため、フロント機能の実装、環境構築を含めてリリースまでを短期間かつ一期通貫で行う
- 低コストで実装できるため、ランダムで表示できる機能も合わせて実装する
- 技術選定
    - MVCモデルフレームワークの使用、クラウド環境の使用を習得する
    - その他、独学のため不明点で作業が止まらないよう、ドキュメントが豊富であることを選定基準とする
        - 環境：AWS（EC2,RDS,ROUTE53）
        - サーバ：nginx,puma
        - 言語：Ruby（Ruby on Rails）

# 2.機能設計

---

## 2-0. 機能概要

---

### 2-0-1. 機能一覧

| 項番 | 機能名称 | 概要 |
| --- | --- | --- |
| 1 | ホーム画面 | ホーム画面 |
| 2 | 図鑑ランダム表示機能 | 世代をキーに、図鑑説明テーブルからデータを取得し画面表示する |
| 3 | 図鑑検索機能 | 「ポケモン名/ソフト」をキーに、図鑑説明テーブルからデータを取得し、画面表示する |
| 4 | スクレイピングツール | 図鑑データ収集用に作成、初回実装時のみ利用対象サイト：https://wiki.xn--rckteqa2e.com/※アクセス数＝ポケモン数となるため1000回程度、　利用ルールには抵触しない |

### 2-0-2. 画面遷移図

![Untitled](./README(no_poke20)%20/Untitled.png)

### 2−0−3. 画面イメージ

![Untitled](./README(no_poke20)%20/Untitled_2.png)

結果画面

![Untitled](./README(no_poke20)%20/Untitled_3.png)

スマートフォン

![Untitled](./README(no_poke20)%20/Untitled_4.png)

### 2-0-4. ER図

![Untitled](./README(no_poke20)%20/Untitled_5.png)

### 2−0−5. AWS構成図

![Untitled](./README(no_poke20)%20/Untitled_6.png)

### 9. ドキュメント一覧

---

| 名称 | 概要 | 備考 |
| --- | --- | --- |
| 機能設計書 | 機能設計（簡易版） | --- |
| データ定義書 | ER図、テーブル定義 |  |
| 画面定義書 | 画面遷移 |  |
| scraping.py | スクレイピングツール | 初回のみ利用ツールのためリファクタリング未済 |