#!/usr/local/bin/perl
# Rage Form Mail Lite (C)2000- exec-R Version 1.00 (2001/03/05)
# As Rage Form Mail version 2.12

#＜Ver 2.11からの変更点＞
#・Ｖｅｒ３．００リリースに伴う名称の変更
#・再投稿処理にクッキーを使用
#・送信者用スキンのみを使用した場合の不具合を解消
#・ｉモードなどの携帯端末での不具合を解消
#・multiple属性つきのセレクトボックスに対応
#・コンマで区切る事で、複数のメールボックスにメールを送信可能

#＜Ver 2.10からの変更点＞
#・設定で送信者に確認のメールを送らないようにできる。
#・送信者と受信者のメールにくっつくメールヘッダ（From）を修正
#・あけましておめでとうございます。今年もよろしくお願いいたします。

#動作不全などがあった場合、ご報告などお願いします。
#スキンやテンプレートファイルを作成する場合は、別ドキュメントをお読みください。
#
#このスクリプトは、不特定多数に悪戯・迷惑メールを送信するのを避けるため、
#メールは一箇所にしか送信できないシステムになっています。
#また、利用者のアクセスログを保存できますので、悪戯メール送信者の調査にも役に立ちますし（プロクシ元の簡易調査機能搭載）、
#これを利用して、二重送信や乱発メール送信も防げます。

#以下は、使用前に決める項目です。
#必要のある項目を適宜変更・追加してください。
#なお、ver 1.00やベータ版からバージョンアップなさった方は、
#
#-----------------------------------------------------------------------------
#Ver 1.00からバージョンアップする際、ここまでは以前と同じ設定でかまいません。
#-----------------------------------------------------------------------------
#
#という表示の部分までは、以前の設定と同じで結構です。

#-----------------------------------------------------------------------------
#☆設定開始☆
#-----------------------------------------------------------------------------

#＜このＣＧＩのＵＲＬ＞
#相対パスでも絶対パスでも構いません。
$bdurl = '/cgi-bin/form-e.cgi';

#sendmailのパスです。各サーバーの説明を読んで、指定してください。
$mailpass = '/usr/lib/sendmail';

#＜利用者のログファイル名＞
#利用者のＩＰアドレス・ホスト名・最終利用時間などを収得するためのファイルです。
#なるべくこのＣＧＩと同じディレクトリに置いてください。
$userlog = 'rfmlog.txt';

#＜利用者ログ保存件数＞
#このくらいが適当ではないかと思われます。
$logmax = 200;

#＜ファイルロック機能＞
#通常は「1」にしておいてください。
#上手く動作しない時は「0」にして下さい。
$lock = 1;

#＜メール送信待ち時間（単位：分）＞
#一回目のメール送信から設定した時間だけ、次のメール送信が出来ないようにします。
#二重送信や悪戯メールの多重送信を防ぐことが出来ます。
$waitmin = 1;

#＜送信先メールアドレス＞
#ここに送信先のメールアドレスを設定してください。
#コンマで区切ることで複数のメールアドレスに配信可能です。
$mailto = 'ebisu@pacifica.ne.jp';

#＜管理者のメールアドレス＞
#メールの返信先に設定されますので、必ず設定してください。
$Ownermail = 'ebisu@pacifica.ne.jp';

#＜メールフォームの名前＞
#メールの差出人に設定されます。任意の名前でどうぞ。
#ですが、３８９行以降の変更により、差出人本人の名前でメールが差し出されます。
$logfrom = '';

#＜管理者名＞
#ここに書かれた管理者あてとしてメールが届きます。
#必須項目ではありませんが、設定した方がよろしいでしょう。

$Owner = 'PACIFICA  EBISU';

#＜ホームページのＵＲＬ＞
#送信確認画面で「送信を取り消す」というスイッチを押した場合に、
#このＵＲＬに戻ります。絶対パスで記入してください。
$homeurl = 'http://www.pacifica.ne.jp/';

#＜メールのタイトル＞
#ここにメールのタイトルを入れてください。
#なお、フォーム側でタイトルを記入させた場合は、
#フォーム側のタイトルの方が優先されます。
$data[0]='お申し込み ＆ お問い合わせ受付';

#＜メールの項目名＞
#$name[1]からはじめて下さい。
#なお、ここではサンプル用の項目名を設定していますので、
#適宜変更・追加してください。
#（追加の際、最後の「;」を忘れないで！！）
#但し、「（記入者の）メールアドレス」だけは設定してはいけません。
#（同梱されているファイル「rfmdoc.txt」の「フォーム作成上の注意」参照）

$name[1]='内容';
$name[2]='お名前';
$name[3]='コース開催日';
$name[4]='コース名';
$name[5]='通信欄';

#＜必須項目にするかどうかのスイッチ＞
#前項「メールの項目名」での変数”$name[n]”が”$need[n]”に対応します。
#「 0・・・任意」、「1・・・必須」となります。
# 例えば、
# $name[1] = 'ハンドルネーム・名前';
# $need[1] = 1;
#↑の場合、「'ハンドルネーム・名前」の項目が必須となります。

$need[1] = 0;
$need[2] = 1;
$need[3] = 0;
$need[4] = 0;
$need[5] = 0;

#＜相手のメールアドレスの記入を必須とするかどうかのスイッチ＞
#「 0・・・任意、メールフォームの記入を設定しない場合もこれ」、「1・・・必須」となります。

$needcc = 1;

#＜メールの総項目数＞
#前項の「メールの項目名」で設定した項目の数をここに入れてください。
$n_of_subject = 5;

#＜内容確認画面などの色設定・背景の設定＞
#ＨＴＭＬタグを記述する要領で変更してください。
#ダブルクォーテーション（""）は取らないで下さい！！
$Body = '<body background="" bgcolor="#FFFFFF" text="#333333">';

#＜登録確認画面のタイトル文字の色＞
$Heco = '#333333';

#＜登録確認画面のタイトルの背景色＞
$Hbco = '#FFFFFF';

#＜登録確認画面の項目表示部分の背景テーブルの色（「項目」の背景色）＞
$Sjco = '#CCCCCC';

#＜登録確認画面の記入内容表示部分の背景テーブルの色（「内容」の背景色）＞
$Ctco = '#FFFFFF';

#＜送信完了画面のメッセージ＞
#
#$notice2 = <<"END_OF_NT";
#（内容を記入する。ここではＨＴＭＬが使えます。）
#END_OF_NT
#
#のように、（）部分をＨＴＭＬを用いて変更してください。
#但し、（）部分の最終行とEND_OF_NTの間には空行を入れないで下さい。
#（正）　　　 （誤）
#</FONT>　　　</FONT>
#END_OF_NT　　
#             END_OF_NT

$notice2 = <<"END_OF_NT";
<table border="0" cellpadding="0" cellspacing="0" width="400"><tr><td><b><font color="#CC0000">ありがとうございました。</font></b><p>後日、担当者からご連絡させていただきます。<br>ご記入いただいたメールアドレスにも、確認メールをお送りしました。</p></td></tr></table>
END_OF_NT

#-----------------------------------------------------------------------------
#ベーター版から移行する際、ここまでは以前と同じ設定で構いません。
#-----------------------------------------------------------------------------

#＜管理人名を非表示にするかどうかのフラグ＞
#０・・・非表示　１・・・表示

$Ow_blank = 1;

#-----------------------------------------------------------------------------
#Ver 1.00からバージョンアップする際、ここまでは以前と同じ設定でかまいません。
#-----------------------------------------------------------------------------


#＜送信先メールアドレスをBccにし、メールヘッダに含ませないようにするかどうかのフラグ＞
#０・・・メールヘッダに含ませない（ＨＰ訪問者にメールアドレスを知らせたくないときに有効です）
#１・・・メールヘッダに含ませる（メールが「To」として送られます）

$send_bcc = 1;

#＜メールのヘッダ文＞
#メールフォームに記入した送信内容の前に書かれます。
#
#$notice2 = <<"END_OF_NT";
#（内容を記入する。改行はメールにそのまま反映されます。）
#END_OF_NT
#
#のように、（）部分を自由に変更してください。
#但し、（）部分の最終行とEND_OF_NTの間には空行を絶対に入れないで下さい。
#（正）　　　　　　　　　　 （誤）
#ありがとうございました　　　ありがとうございました
#END_OF_NT　　
#             			　　 END_OF_NT

$mailheader = <<'END_OF_NT';
以下がメールフォームの内容です。
END_OF_NT

#＜メールのフッダー文＞
#メールフォームに記入した送信内容の後に書かれます。
#書法はヘッダ文に同じです

$mailfooder = <<'END_OF_NT';
以上の内容でメールが送信されました。
ご利用ありがとうございました。
END_OF_NT

#-----------------------------------------------------------------------------
#Ver 1.05/06からバージョンアップする際、ここまでは以前と同じ設定でかまいません。
#-----------------------------------------------------------------------------

#＜確認画面・完了画面の幅＞
#%指定でも、ピクセル数でもお好きな方法で変更できます。

$width = '400'; 

#＜確認画面スキップフラグ＞
#０・・・確認画面を表示せず、送信者に記入内容を確認させない
#１・・・確認画面を表示し、送信者に記入内容を確認させる

$chk_skip = 1; 

#-----------------------------------------------------------------------------
#Ver 1.07/08/09,Ver 2.00 からバージョンアップする際、ここまでは以前と同じ設定でかまいません。
#Ver 2.10/2.11 で新たに増えた設定事項には、「※Ver 2.10新設」とかかれてあります。
#-----------------------------------------------------------------------------

#＜受信者用テンプレートファイル名＞
#受け取るメールをテンプレートを使って送信したい場合は、
#ここにそのテンプレートファイルのファイル名を入れてください
#テンプレートを利用しない場合は、何も記入しないで下さい。

$mailformat = 'owner.txt';

#＜発信・投稿者用テンプレートファイル名＞  ※Ver 2.10新設
#送信した方にコピーではなく、別の書式でメールを送りたい場合は、
#ここにその書式を書いたテンプレートファイルのファイル名を入れてください
#受信者と送信者のメールが同じで構わない場合は、何も記入しないで下さい。

$mailformat2 = 'sender.txt';

#＜確認画面のスキンファイル名＞
#確認画面にスキンを使用なさりたい場合は、
#ここにそのスキンファイルのファイル名を入れてください
#スキンを利用しない場合は、何も記入しないで下さい。

$checkhtml = '';

#＜エラー画面のスキンファイル名＞
#エラー画面にスキンを使用なさりたい場合は、
#ここにそのスキンファイルのファイル名を入れてください
#スキンを利用しない場合は、何も記入しないで下さい。

$errorhtml = '';

#＜エラー項目の仕切り＞
#エラー画面にスキンを使用なさる場合、
#ここにエラー項目の仕切りとなる文字を入れてください
#
#「$itempartion = '★';」とすると、
#［名前］★［ＵＲＬ］★［コメント］
#というように表示されます。

$itempartion = '<li>';

#＜送信終了画面のＵＲＬ＞
#送信終了画面を別途他のＨＴＭＬになさる場合は、
#ここにその送信終了画面のＵＲＬを絶対パスで入れてください
#
#（例）
#$thankshtmlurl = 'http://www.we-box.com/cgi/thanks.html';
#
#この機能を利用しない場合は、何も記入しないで下さい。

$thankshtmlurl = '';

#＜外部利用禁止のための、フォームのＵＲＬ＞
#フォームの外部利用を禁止するためには、
#フォームのＨＴＭＬを設置したＵＲＬをここで設定してください。
#ただ、この機能を有効にすると一部のブラウザで動作不全が起こる場合がございます。
#ＵＲＬは”絶対パス”でお願い致します。
#
#（例）
#$formhtmlurl = 'http://www.we-box.com/cgi/rfmsap1.html';
#

$formhtmlurl = '';

#＜送信者の詳細情報をメールに表示する＞  ※Ver 2.10新設
#送信した方のＩＰアドレスなどの情報をメールに表示するかどうかのフラグです。
#メールテンプレート機能をご利用の場合は、このフラグは効果ありません。
#（別途 <!-- senderinfo -->タグをメールテンプレートに入れてください。）
#０・・・非表示　１・・・表示

$senderinfo = 1;


#＜送信者にコピーメールを送るかどうかのフラグ＞  ※Ver 2.11新設
#送信した方にコピーメールを送るかどうかのフラグです。
#発信・投稿者用テンプレートをご利用の場合は、このフラグは効果ありません。
#０・・・送らない　１・・・送る

$copymail = 1;

#４４７行以降にも、修正項目（送信者の名前でメールを送るかどうか）がございます。
#更なるカスタマイズをお求めの方は、是非ご覧下さい。

#----------------------------------------------------------------------------
#変更項目、ここまで。
#
#これ以降は改造を試みる時以外変更しないで下さい。
#なお、改造の際は自己責任にてお願い致します。
#（改造の際のアドバイスは致しますので、お気軽にご相談下さい。）
#-----------------------------------------------------------------------------

#変数の初期化

local($ctime,$sdata,$default_checkhtml,$default_errorhtml,$Encoding,$CharSet,$viewall,$source_of_mail);
local($mode,$i,$ref,$uri,$let_miss,$errortype);#my
#local(@data);
local(%in,%cookie,$tipad,$thost,$rfmuser);

$rfmuser = 'rfmliteuser';
$name[0] = 'メールの題名';
$need[0] = 1; #メール題名は必須！！
$Encoding = 'sjis';#文字コード。
$CharSet = 'shift_jis';#文字コード。表示用です。
$ctime = time;

$copyright = '・RAGE FORM MAIL Lite Version 1.00 Copyright(C) 2000,2001 By <a href="http://www.we-box.com/" target="_top">WE-BOX</a>';
#著作権表示です。許可無く変更した場合はスクリプトの使用を認めません。

require 'r_util.pl';#汎用サブルーチンの準備
require 'jcode.pl';#日本語処理ルーチンの準備

&defhtml();#デフォルトのＨＴＭＬを読み込む
&parseinput($Encoding);#取り込み
$mode = $in{'mode'};
&getlog();#送信者ログ収得

#外部利用チェック
$ref = $ENV{'HTTP_REFERER'};
$uri = $ENV{'REQUEST_URI'};
$ref =~ s/%7E/~/ig;
$uri =~ s/%7E/~/ig;
if ($formhtmlurl && ( ($ENV{'REQUEST_METHOD'} !~ /POST/i) || ($ref !~ /$formhtmlurl/i && !$mode) || ($ref !~ /$formhtmlurl/i && !$chk_skip) || ($ref !~ /$uri/i && $mode eq 'post') ) ) {
	&o_g_illgal('外部からの利用はできません','決められたフォームを経由しない、不正な外部からの利用はできません。<br>決められたフォームから送信して下さい。',0);
}
#データチェッカ用に、フォームから書き込んだ内容を取り込む。
for ($i=1;$i<=$n_of_subject+1;$i++) {
    $data[$i] = &coding_fbd($in{"data$i"});
}

#メールアドレスを取り込む
$mailcc = $in{'mailcc'};

#題名を取り込む
$data[0] = $in{'data0'} if ($in{'data0'});

#内容のチェック
if (&posttimeparam()) {
    &o_g_illgal('P A C I F I C A____________________エラー！','一定時間待ってから再度送信してください。',0);
}

#送信モードかどうか確認
&posting() if ($mode eq 'post');

#メールアドレスの形式確認
if ($mailcc && $mailcc !~ /^[\w\+\-\.]+@[\w\+\-]+\.[\w\+\.\-]+$/) {
    &o_g_illgal('P A C I F I C A____________________エラー！',"入力されたメールアドレスに間違いがあります。<br>内容を確認してから、もう一度やり直してください。",0);
}

#確認画面の描画と内容確認
$let_miss = &ch_post();
if ($let_miss) {&o_g_illgal('P A C I F I C A____________________エラー！',$let_miss,1);}
&posting() if (!$chk_skip);
$errortype = "P A C I F I C A____________________内容確認";
print "Content-type: text/html\n\n";
#デフォルト用の確認画面を作る
$viewall = "<table border=1 cellpadding=5 cellspacing=0 width=400 bordercolor=\"$Hbco\">";
$viewall.= "<tr><th bgcolor=\"$Sjco\">項目</td><th bgcolor=\"$Ctco\">内容</td></tr>\n";
for ($i=0;$i<@data-1;$i++) {
    $viewall .= "<tr><td bgcolor=\"$Sjco\">$name[$i]</td><td bgcolor=\"$Ctco\">$data[$i]</td></tr>\n";
}
if ($mailcc) {
    $viewall .= "<tr><td bgcolor=\"$Sjco\">メールアドレス</td><td bgcolor=\"$Ctco\">$mailcc</td></tr>\n";
}
$viewall .= "</table>\n";

#送信用のメールソース
$source_of_mail = "<input type=hidden name=mode value=post>\n";
for ($i=0;$i<@data;$i++) {
    $source_of_mail .= "<input type=hidden name=data$i value=\"$data[$i]\">\n";
}
$source_of_mail .= "<input type=hidden name=mailcc value=\"$mailcc\">\n";

#確認画面を表示して終わり
print &tranceskin($checkhtml,$default_checkhtml);
exit(0);

#エラー処理
sub o_g_illgal {
	local($errortype,$errorcontent,$et_sub) =@_;
	print "Content-type: text/html\n\n";
	if ($et_sub) {
		$dealwitherror = '記入もれがあります。（必須）と書かれた項目は必ずご記入ください。<br><br><a href="javascript:history.back();">B A C K</a>';
	} else {
		$dealwitherror = 'メール送信に失敗しました。エラー内容をよくお読みになって、再度お試しください。<br><br><a href="javascript:history.back();">B A C K</a>';
	}
	print &tranceskin($errorhtml,$default_errorhtml);
	exit(0);
}

#メール発信処理
sub posting {
	local ($mailcontent,$mailcontent2,$mailheadinfo,$sendinfo,$post_from,$co_mailto);#my
	local ($tmp,$i,$ctdate,$cttime,$agent,$p_ls,$p_lf,$p_Ow,$cc1);#my
	local (@sendto);
	for ($i=1;$i<=$n_of_subject+1;$i++) {
    	$data[$i] = &coding_fbd2($in{"data$i"});
	}
	&putlog();
	if ($mailcc) {
		$post_from = $mailcc;
	} else {
		$post_from = $Ownermail;
	}
	$p_ls = &e_base64("$data[0]");
	$p_Ow = &e_base64("$Owner");
	$ctdate = &stringfromtime(time + 9 * 3600,' ','+0900');
	$cttime = gmtime(time + 9 * 3600);
	$agent = substr($ENV{'HTTP_USER_AGENT'},0,200);
	$sendinfo = 
'送信時間        　  : '.$cttime."\n".
'ホスト名            : '.$thost."\n".
'ＩＰアドレス　　　　: '.$tipad."\n".
'利用ブラウザ        : '.$agent."\n".
'要求されたメソッド　: '.$ENV{'REQUEST_METHOD'}."\n".
'スクリプト名・ＵＲＬ: '.$ENV{'SCRIPT_NAME'}."\n".
'参照元ＵＲＬ     　 : '.$ENV{'HTTP_REFERER'}."\n".
'サーバの名前    　  : '.$ENV{'SERVER_NAME'}."\n".
'サーバーのプロトコル: '.$ENV{'SERVER_PROTOCOL'}."\n".
'サーバのポート番号　: '.$ENV{'SERVER_PORT'}."\n";

#更なる設定事項
#以下の２行の「$logfrom」と「$Owner」を、
#フォームで名前を記入させる際に指定したデーター番号にしたがって修正すると、
#送信者の記入した名前でメールが送れます。
#
#基本は、
#
# $p_lf = &e_base64("$data[（データー番号）]");
#
#
#例えば、名前のところを<input type="text" name="data2">とした場合、
#
# $p_lf = &e_base64("$data[2]");
#
#と、変更してください。

	$p_lf = &e_base64("$data[2]");

#ヘッダ部分を作る
$mailheadinfo = <<"END_OF_MH";
Date: $ctdate
Subject: $p_ls
X-HTTP-REFERER: $ref
X-HTTP-USER-AGENT: $agent
X-REMOTE-ADDR: $tipad
X-REMOTE-HOST: $thost
X-Mailer: Rage Form Mail Lite ver 1.00_212 (http://www.we-box.com/)
MIME-Version: 1.0
Content-Type: text/plain; charset=iso-2022-jp
Content-Transfer-Encoding: 7bit
END_OF_MH

	#送信先処理
	@sendto = split(/,/,$mailto);
	$mailto = shift(@sendto);
	foreach $tmp (@sendto) {
		$co_mailto .= "Cc: $tmp\n";
	}
	#コピーメール処理
	$cc1 = '';
	$cc1 = "From: $p_Ow<$Ownermail>\nReply-To: $p_Ow<$Ownermail>\n" if ($send_bcc);
	
	#本文を作る
	if (!$mailformat) {
		$mailcontent .= $mailheader;
		$mailcontent .= "\n\n";
		for ($i=1;$i<@data-1;$i++) {
    		$mailcontent .="$name[$i]\n$data[$i]\n\n";
		}
		if ($mailcc) {
			$mailcontent .= '相手のメールアドレス'."\n$mailcc\n\n";
		}
		$mailcontent .= $mailfooder;
		if ($senderinfo) {
			$mailcontent .= "\n \n";
			$mailcontent .= '-' x 60;
			$mailcontent .= "\n";
			$mailcontent .= $sendinfo;
			$mailcontent .= '-' x 60;
		}
	} else {
		$mailcontent = &tranceskin($mailformat,'');
	}
	$mailcontent2 = &tranceskin($mailformat2,'') if ($mailformat2);
	
	#ヘッダと本文を合成する
	$mailcontent2 = $mailcontent if (!$mailformat2);
	$mailcontent  = "To: $p_Ow<$mailto>\n$co_mailto"."From: $p_lf<$post_from>\nReply-To: $p_lf<$post_from>\n".$mailheadinfo."\n".$mailcontent;
	$mailcontent2 = "To: $mailcc\n$cc1".$mailheadinfo."\n".$mailcontent2 if ($copymail);

	#メールを送る
	&jcode'convert(*mailcontent,'jis');
	open (MAIL, "| $mailpass -t");
#or die "メール送信失敗\n";
	print MAIL $mailcontent;
	close (MAIL);

	if ($copymail) {
		&jcode'convert(*mailcontent2,'jis');
		open (MAIL, "| $mailpass -t");
	#or die "メール送信失敗\n";
		print MAIL $mailcontent2;
		close (MAIL);
	}
	#クッキーに再送信防止用のデーターを書き込んでおく
	undef %cookie;
	$cookie{'lastposttime'} = $ctime;
	&put_Cookie($rfmuser,30);
	
	#送信終了画面表示
    print "Location: $thankshtmlurl\n\n" if ($thankshtmlurl);
	print "Content-type: text/html\n\n";
	$errortype = "P A C I F I C A____________________送信完了";
	$ts_out =~ s/<!-- errorcontent -->/$errorcontent/gi;
	$ts_out =~ s/<!-- dealwitherror -->/$dealwitherror/gi;
	$dealwitherror = $notice2;
	$errorcontent = "<a href=\"$homeurl\"><b>B A C K</b></a>";
	print &tranceskin('',$default_errorhtml);
#print "<form><textarea cols=80 rows=10>$mailcontent</textarea></form>";#デバッグ
#print "<form><textarea cols=80 rows=10>$mailcontent2</textarea></form>";#デバッグ
	exit(0);
}

#スキン変換ルーチン
sub tranceskin {
	local ($ts_file,$ts_out) = @_;#my
	local ($i,$ownerinfo);#my
	$ts_out = &loadskin($ts_file) if ($ts_file);
	#項目＆記入内容の置き換え
	for ($i=0;$i<=$n_of_subject+1;$i++) {
		$ts_out =~ s/<!-- data$i -->/$data[$i]/gi;
		$ts_out =~ s/<!-- name$i -->/$name[$i]/gi;
	}
	$ts_out =~ s/<!-- mailcc -->/$mailcc/gi;
	#ヘッダ文＆フッダの文の置き換え
	$ts_out =~ s/<!-- header -->/$mailheader/gi;
	$ts_out =~ s/<!-- fooder -->/$mailfooder/gi;
	#エラー文と、エラー内容の置き換え
	$ts_out =~ s/<!-- error -->/$errortype/gi;
	$ts_out =~ s/<!-- errorcontent -->/$errorcontent/gi;
	$ts_out =~ s/<!-- dealwitherror -->/$dealwitherror/gi;
	#確認画面から送信画面に、書いた内容を渡すための記号
	$ts_out =~ s/<!-- mailcontent -->/$source_of_mail/gi;
	#テーブルを使って、一気に確認内容を表示するための記号
	$ts_out =~ s/<!-- viewall -->/$viewall/gi;
	#著作権表示と管理者表示・投稿者情報表示
	$ownerinfo = "<a href=\"mailto:$Ownermail\">$Owner</a>";
	$ts_out =~ s/<!-- ownerinfo -->/$ownerinfo/gi if ($Ow_blank);
	$ts_out =~ s/<!-- copyright -->/$copyright/gi;
	$ts_out =~ s/<!-- senderinfo -->/$sendinfo/gi;
	return $ts_out;
}

#表示のための文字変換ルーチン
sub coding_fbd {
    local($string) = @_;#my
    $string =~ s/&/&amp;/g;
    $string =~ s/"/&quot;/g;
    $string =~ s/</&lt;/g;
    $string =~ s/>/&gt;/g;
    $string =~ s/,/&#44;/g;
    $string =~ s/\r\n/\n/g;
    $string =~ s/\r/\n/g;
    $string =~ s/\n\n/<br> <br>/g;
    $string =~ s/\n/<br>/g;
    return $string;
}


sub coding_fbd2 {
    local($string) = @_;#my
    $string =~ s/<br>/\n/g;#お使いの機種によって変更願います
	$string =~ s/&amp;/&/g;
	$string =~ s/&quot;/"/g;
	$string =~ s/&lt;/</g;
	$string =~ s/&gt;/>/g;
	$string =~ s/&#44;/,/g;
    return $string;
}

#エラー内容生成ルーチン

sub ch_post {
    local($i,$cp_out);#my
    for ($i=0;$i<@data-1;$i++) {
        if ($need[$i] && !$data[$i]) {
        $cp_out .= $itempartion.'［'.$name[$i].'］';
        }
    }
    if ($needcc && !$mailcc) {
        $cp_out .= $itempartion.'［メールアドレス］';
    }
return $cp_out;
}

#多重投稿防止のためのルーチン

#ログを取る
sub getlog {
    local ($gl_ipad1,$gl_ipad2);
    $gl_ipad1 = $ENV{'HTTP_X_FORWARDED_FOR'};
    $gl_ipad2 = $ENV{'REMOTE_ADDR'};
    if ($gl_ipad1) {
        $tipad = $gl_ipad1;
    } else {
        $tipad = $gl_ipad2;
    }
    $thost = gethostbyaddr(pack("C4", split(/\./, $tipad)), 2);
    $sdata = "$tipad,$thost,$ctime\n";
}

#ログを読む
sub putlog {
	local(@tdata);#my
    &lock_open(LOG, "+<$userlog");
    @tdata = <LOG>;
    unshift(@tdata , $sdata);
    splice(@tdata,$logmax);
    seek(LOG, 0, 0);
    print LOG @tdata;
    truncate(LOG, tell(LOG));
    &unlock_close(LOG);
}

#時間判定
sub posttimeparam {
    local($i,$ptm_time,@tdata);#my
	&get_Cookie($rfmuser);
	$ptm_time = $cookie{'lastposttime'};
	return 1 if ($ctime - $ptm_time <= $waitmin*60);
	
    open(LOG, "$userlog");
    @tdata = <LOG>;
    close(LOG);
    for ($i=0;$i<@tdata;$i++) {
        local($ptm_ipad,$ptm_host,$ptm_time) = split(/,/,$tdata[$j]);
        if ($ctime - $ptm_time > $waitmin*60 ) {
            last;
        } elsif ($ptm_ipad eq $tipad && $ptm_host eq $thost && $ctime - $ptm_time <= $waitmin*60) {
        return 1;
        }
    }
    return 0;
}

#デフォルトのＨＴＭＬ内容

sub defhtml {

local($dh_tco,$dh_lco,$dh_bgc,$htmlheader,$headermc,$foodermc);#my
$dh_tco =$Body;
$dh_lco =$Body;
$dh_bgc =$Body;
$dh_tco =~ s/.+TEXT="(.......)".+/$1/i;
$dh_lco =~ s/.+ LINK="(.......)".+/$1/i;
$dh_bgc =~ s/.+BGCOLOR="(.......)".+/$1/i;

#スタイルシート記述
$htmlheader = <<"END_OF_NT";
END_OF_NT

#ヘッダ部分マクロ
$headermc = <<"END_OF_NT";
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=$CharSet">
<title><!-- error --></title>
$htmlheader
</head>
$Body
<div align="center">
END_OF_NT

#フッダ部分マクロ
$foodermc = <<"END_OF_NT";
END_OF_NT

#確認画面用のＨＴＭＬ
$default_checkhtml = <<"END_OF_NT";
$headermc
<table width=$width><tr><th bgcolor=$Hbco>
</td></tr>
<tr><td>
<b><font color="#CC0000">下記の内容で送信します。もう一度ご確認ください。</font></b><br><br>
<!-- viewall -->
<br>
<table><tr><td>
<form action=$bdurl method=POST>
<!-- mailcontent -->
<input type=submit value="　送信　"></form>
</td><td>
<input type=submit name value="　戻る　" onclick="JavaScript:history.back();"></p>
</td></tr></table>
</td></tr></table></div>
</body></html>
END_OF_NT

#エラー内容のＨＴＭＬ
$default_errorhtml = <<"END_OF_NT";
$headermc
<table width=$width>
<tr><td>
<!-- dealwitherror -->
<br><b><font color="#FF0000"><!-- errorcontent --></font></b>
<br>
</td></tr></table></div>
</body></html>
END_OF_NT
}
