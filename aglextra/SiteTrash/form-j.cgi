#!/usr/local/bin/perl
# Rage Form Mail Lite (C)2000- exec-R Version 1.00 (2001/03/05)
# As Rage Form Mail version 2.12

#��Ver 2.11����̕ύX�_��
#�E�u�����R�D�O�O�����[�X�ɔ������̂̕ύX
#�E�ē��e�����ɃN�b�L�[���g�p
#�E���M�җp�X�L���݂̂��g�p�����ꍇ�̕s�������
#�E�����[�h�Ȃǂ̌g�ђ[���ł̕s�������
#�Emultiple�������̃Z���N�g�{�b�N�X�ɑΉ�
#�E�R���}�ŋ�؂鎖�ŁA�����̃��[���{�b�N�X�Ƀ��[���𑗐M�\

#��Ver 2.10����̕ύX�_��
#�E�ݒ�ő��M�҂Ɋm�F�̃��[���𑗂�Ȃ��悤�ɂł���B
#�E���M�҂Ǝ�M�҂̃��[���ɂ��������[���w�b�_�iFrom�j���C��
#�E�����܂��Ă��߂łƂ��������܂��B���N����낵�����肢�������܂��B

#����s�S�Ȃǂ��������ꍇ�A���񍐂Ȃǂ��肢���܂��B
#�X�L����e���v���[�g�t�@�C�����쐬����ꍇ�́A�ʃh�L�������g�����ǂ݂��������B
#
#���̃X�N���v�g�́A�s���葽���Ɉ��Y�E���f���[���𑗐M����̂�����邽�߁A
#���[���͈�ӏ��ɂ������M�ł��Ȃ��V�X�e���ɂȂ��Ă��܂��B
#�܂��A���p�҂̃A�N�Z�X���O��ۑ��ł��܂��̂ŁA���Y���[�����M�҂̒����ɂ����ɗ����܂����i�v���N�V���̊ȈՒ����@�\���ځj�A
#����𗘗p���āA��d���M�◐�����[�����M���h���܂��B

#�ȉ��́A�g�p�O�Ɍ��߂鍀�ڂł��B
#�K�v�̂��鍀�ڂ�K�X�ύX�E�ǉ����Ă��������B
#�Ȃ��Aver 1.00��x�[�^�ł���o�[�W�����A�b�v�Ȃ��������́A
#
#-----------------------------------------------------------------------------
#Ver 1.00����o�[�W�����A�b�v����ہA�����܂ł͈ȑO�Ɠ����ݒ�ł��܂��܂���B
#-----------------------------------------------------------------------------
#
#�Ƃ����\���̕����܂ł́A�ȑO�̐ݒ�Ɠ����Ō��\�ł��B

#-----------------------------------------------------------------------------
#���ݒ�J�n��
#-----------------------------------------------------------------------------

#�����̂b�f�h�̂t�q�k��
#���΃p�X�ł���΃p�X�ł��\���܂���B
$bdurl = '/cgi-bin/form-e.cgi';

#sendmail�̃p�X�ł��B�e�T�[�o�[�̐�����ǂ�ŁA�w�肵�Ă��������B
$mailpass = '/usr/lib/sendmail';

#�����p�҂̃��O�t�@�C������
#���p�҂̂h�o�A�h���X�E�z�X�g���E�ŏI���p���ԂȂǂ��������邽�߂̃t�@�C���ł��B
#�Ȃ�ׂ����̂b�f�h�Ɠ����f�B���N�g���ɒu���Ă��������B
$userlog = 'rfmlog.txt';

#�����p�҃��O�ۑ�������
#���̂��炢���K���ł͂Ȃ����Ǝv���܂��B
$logmax = 200;

#���t�@�C�����b�N�@�\��
#�ʏ�́u1�v�ɂ��Ă����Ă��������B
#��肭���삵�Ȃ����́u0�v�ɂ��ĉ������B
$lock = 1;

#�����[�����M�҂����ԁi�P�ʁF���j��
#���ڂ̃��[�����M����ݒ肵�����Ԃ����A���̃��[�����M���o���Ȃ��悤�ɂ��܂��B
#��d���M�∫�Y���[���̑��d���M��h�����Ƃ��o���܂��B
$waitmin = 1;

#�����M�惁�[���A�h���X��
#�����ɑ��M��̃��[���A�h���X��ݒ肵�Ă��������B
#�R���}�ŋ�؂邱�Ƃŕ����̃��[���A�h���X�ɔz�M�\�ł��B
$mailto = 'ebisu@pacifica.ne.jp';

#���Ǘ��҂̃��[���A�h���X��
#���[���̕ԐM��ɐݒ肳��܂��̂ŁA�K���ݒ肵�Ă��������B
$Ownermail = 'ebisu@pacifica.ne.jp';

#�����[���t�H�[���̖��O��
#���[���̍��o�l�ɐݒ肳��܂��B�C�ӂ̖��O�łǂ����B
#�ł����A�R�W�X�s�ȍ~�̕ύX�ɂ��A���o�l�{�l�̖��O�Ń��[���������o����܂��B
$logfrom = '';

#���Ǘ��Җ���
#�����ɏ����ꂽ�Ǘ��҂��ĂƂ��ă��[�����͂��܂��B
#�K�{���ڂł͂���܂��񂪁A�ݒ肵��������낵���ł��傤�B

$Owner = 'PACIFICA  EBISU';

#���z�[���y�[�W�̂t�q�k��
#���M�m�F��ʂŁu���M���������v�Ƃ����X�C�b�`���������ꍇ�ɁA
#���̂t�q�k�ɖ߂�܂��B��΃p�X�ŋL�����Ă��������B
$homeurl = 'http://www.pacifica.ne.jp/';

#�����[���̃^�C�g����
#�����Ƀ��[���̃^�C�g�������Ă��������B
#�Ȃ��A�t�H�[�����Ń^�C�g�����L���������ꍇ�́A
#�t�H�[�����̃^�C�g���̕����D�悳��܂��B
$data[0]='���\������ �� ���₢���킹��t';

#�����[���̍��ږ���
#$name[1]����͂��߂ĉ������B
#�Ȃ��A�����ł̓T���v���p�̍��ږ���ݒ肵�Ă��܂��̂ŁA
#�K�X�ύX�E�ǉ����Ă��������B
#�i�ǉ��̍ہA�Ō�́u;�v��Y��Ȃ��ŁI�I�j
#�A���A�u�i�L���҂́j���[���A�h���X�v�����͐ݒ肵�Ă͂����܂���B
#�i��������Ă���t�@�C���urfmdoc.txt�v�́u�t�H�[���쐬��̒��Ӂv�Q�Ɓj

$name[1]='���e';
$name[2]='�����O';
$name[3]='�R�[�X�J�Ó�';
$name[4]='�R�[�X��';
$name[5]='�ʐM��';

#���K�{���ڂɂ��邩�ǂ����̃X�C�b�`��
#�O���u���[���̍��ږ��v�ł̕ϐ��h$name[n]�h���h$need[n]�h�ɑΉ����܂��B
#�u 0�E�E�E�C�Ӂv�A�u1�E�E�E�K�{�v�ƂȂ�܂��B
# �Ⴆ�΁A
# $name[1] = '�n���h���l�[���E���O';
# $need[1] = 1;
#���̏ꍇ�A�u'�n���h���l�[���E���O�v�̍��ڂ��K�{�ƂȂ�܂��B

$need[1] = 0;
$need[2] = 1;
$need[3] = 0;
$need[4] = 0;
$need[5] = 0;

#������̃��[���A�h���X�̋L����K�{�Ƃ��邩�ǂ����̃X�C�b�`��
#�u 0�E�E�E�C�ӁA���[���t�H�[���̋L����ݒ肵�Ȃ��ꍇ������v�A�u1�E�E�E�K�{�v�ƂȂ�܂��B

$needcc = 1;

#�����[���̑����ڐ���
#�O���́u���[���̍��ږ��v�Őݒ肵�����ڂ̐��������ɓ���Ă��������B
$n_of_subject = 5;

#�����e�m�F��ʂȂǂ̐F�ݒ�E�w�i�̐ݒ聄
#�g�s�l�k�^�O���L�q����v�̂ŕύX���Ă��������B
#�_�u���N�H�[�e�[�V�����i""�j�͎��Ȃ��ŉ������I�I
$Body = '<body background="" bgcolor="#FFFFFF" text="#333333">';

#���o�^�m�F��ʂ̃^�C�g�������̐F��
$Heco = '#333333';

#���o�^�m�F��ʂ̃^�C�g���̔w�i�F��
$Hbco = '#FFFFFF';

#���o�^�m�F��ʂ̍��ڕ\�������̔w�i�e�[�u���̐F�i�u���ځv�̔w�i�F�j��
$Sjco = '#CCCCCC';

#���o�^�m�F��ʂ̋L�����e�\�������̔w�i�e�[�u���̐F�i�u���e�v�̔w�i�F�j��
$Ctco = '#FFFFFF';

#�����M������ʂ̃��b�Z�[�W��
#
#$notice2 = <<"END_OF_NT";
#�i���e���L������B�����ł͂g�s�l�k���g���܂��B�j
#END_OF_NT
#
#�̂悤�ɁA�i�j�������g�s�l�k��p���ĕύX���Ă��������B
#�A���A�i�j�����̍ŏI�s��END_OF_NT�̊Ԃɂ͋�s�����Ȃ��ŉ������B
#�i���j�@�@�@ �i��j
#</FONT>�@�@�@</FONT>
#END_OF_NT�@�@
#             END_OF_NT

$notice2 = <<"END_OF_NT";
<table border="0" cellpadding="0" cellspacing="0" width="400"><tr><td><b><font color="#CC0000">���肪�Ƃ��������܂����B</font></b><p>����A�S���҂��炲�A�������Ă��������܂��B<br>���L���������������[���A�h���X�ɂ��A�m�F���[���������肵�܂����B</p></td></tr></table>
END_OF_NT

#-----------------------------------------------------------------------------
#�x�[�^�[�ł���ڍs����ہA�����܂ł͈ȑO�Ɠ����ݒ�ō\���܂���B
#-----------------------------------------------------------------------------

#���Ǘ��l�����\���ɂ��邩�ǂ����̃t���O��
#�O�E�E�E��\���@�P�E�E�E�\��

$Ow_blank = 1;

#-----------------------------------------------------------------------------
#Ver 1.00����o�[�W�����A�b�v����ہA�����܂ł͈ȑO�Ɠ����ݒ�ł��܂��܂���B
#-----------------------------------------------------------------------------


#�����M�惁�[���A�h���X��Bcc�ɂ��A���[���w�b�_�Ɋ܂܂��Ȃ��悤�ɂ��邩�ǂ����̃t���O��
#�O�E�E�E���[���w�b�_�Ɋ܂܂��Ȃ��i�g�o�K��҂Ƀ��[���A�h���X��m�点�����Ȃ��Ƃ��ɗL���ł��j
#�P�E�E�E���[���w�b�_�Ɋ܂܂���i���[�����uTo�v�Ƃ��đ����܂��j

$send_bcc = 1;

#�����[���̃w�b�_����
#���[���t�H�[���ɋL���������M���e�̑O�ɏ�����܂��B
#
#$notice2 = <<"END_OF_NT";
#�i���e���L������B���s�̓��[���ɂ��̂܂ܔ��f����܂��B�j
#END_OF_NT
#
#�̂悤�ɁA�i�j���������R�ɕύX���Ă��������B
#�A���A�i�j�����̍ŏI�s��END_OF_NT�̊Ԃɂ͋�s���΂ɓ���Ȃ��ŉ������B
#�i���j�@�@�@�@�@�@�@�@�@�@ �i��j
#���肪�Ƃ��������܂����@�@�@���肪�Ƃ��������܂���
#END_OF_NT�@�@
#             			�@�@ END_OF_NT

$mailheader = <<'END_OF_NT';
�ȉ������[���t�H�[���̓��e�ł��B
END_OF_NT

#�����[���̃t�b�_�[����
#���[���t�H�[���ɋL���������M���e�̌�ɏ�����܂��B
#���@�̓w�b�_���ɓ����ł�

$mailfooder = <<'END_OF_NT';
�ȏ�̓��e�Ń��[�������M����܂����B
�����p���肪�Ƃ��������܂����B
END_OF_NT

#-----------------------------------------------------------------------------
#Ver 1.05/06����o�[�W�����A�b�v����ہA�����܂ł͈ȑO�Ɠ����ݒ�ł��܂��܂���B
#-----------------------------------------------------------------------------

#���m�F��ʁE������ʂ̕���
#%�w��ł��A�s�N�Z�����ł����D���ȕ��@�ŕύX�ł��܂��B

$width = '400'; 

#���m�F��ʃX�L�b�v�t���O��
#�O�E�E�E�m�F��ʂ�\�������A���M�҂ɋL�����e���m�F�����Ȃ�
#�P�E�E�E�m�F��ʂ�\�����A���M�҂ɋL�����e���m�F������

$chk_skip = 1; 

#-----------------------------------------------------------------------------
#Ver 1.07/08/09,Ver 2.00 ����o�[�W�����A�b�v����ہA�����܂ł͈ȑO�Ɠ����ݒ�ł��܂��܂���B
#Ver 2.10/2.11 �ŐV���ɑ������ݒ莖���ɂ́A�u��Ver 2.10�V�݁v�Ƃ�����Ă���܂��B
#-----------------------------------------------------------------------------

#����M�җp�e���v���[�g�t�@�C������
#�󂯎�郁�[�����e���v���[�g���g���đ��M�������ꍇ�́A
#�����ɂ��̃e���v���[�g�t�@�C���̃t�@�C���������Ă�������
#�e���v���[�g�𗘗p���Ȃ��ꍇ�́A�����L�����Ȃ��ŉ������B

$mailformat = 'owner.txt';

#�����M�E���e�җp�e���v���[�g�t�@�C������  ��Ver 2.10�V��
#���M�������ɃR�s�[�ł͂Ȃ��A�ʂ̏����Ń��[���𑗂肽���ꍇ�́A
#�����ɂ��̏������������e���v���[�g�t�@�C���̃t�@�C���������Ă�������
#��M�҂Ƒ��M�҂̃��[���������ō\��Ȃ��ꍇ�́A�����L�����Ȃ��ŉ������B

$mailformat2 = 'sender.txt';

#���m�F��ʂ̃X�L���t�@�C������
#�m�F��ʂɃX�L�����g�p�Ȃ��肽���ꍇ�́A
#�����ɂ��̃X�L���t�@�C���̃t�@�C���������Ă�������
#�X�L���𗘗p���Ȃ��ꍇ�́A�����L�����Ȃ��ŉ������B

$checkhtml = '';

#���G���[��ʂ̃X�L���t�@�C������
#�G���[��ʂɃX�L�����g�p�Ȃ��肽���ꍇ�́A
#�����ɂ��̃X�L���t�@�C���̃t�@�C���������Ă�������
#�X�L���𗘗p���Ȃ��ꍇ�́A�����L�����Ȃ��ŉ������B

$errorhtml = '';

#���G���[���ڂ̎d�؂聄
#�G���[��ʂɃX�L�����g�p�Ȃ���ꍇ�A
#�����ɃG���[���ڂ̎d�؂�ƂȂ镶�������Ă�������
#
#�u$itempartion = '��';�v�Ƃ���ƁA
#�m���O�n���m�t�q�k�n���m�R�����g�n
#�Ƃ����悤�ɕ\������܂��B

$itempartion = '<li>';

#�����M�I����ʂ̂t�q�k��
#���M�I����ʂ�ʓr���̂g�s�l�k�ɂȂ���ꍇ�́A
#�����ɂ��̑��M�I����ʂ̂t�q�k���΃p�X�œ���Ă�������
#
#�i��j
#$thankshtmlurl = 'http://www.we-box.com/cgi/thanks.html';
#
#���̋@�\�𗘗p���Ȃ��ꍇ�́A�����L�����Ȃ��ŉ������B

$thankshtmlurl = '';

#���O�����p�֎~�̂��߂́A�t�H�[���̂t�q�k��
#�t�H�[���̊O�����p���֎~���邽�߂ɂ́A
#�t�H�[���̂g�s�l�k��ݒu�����t�q�k�������Őݒ肵�Ă��������B
#�����A���̋@�\��L���ɂ���ƈꕔ�̃u���E�U�œ���s�S���N����ꍇ���������܂��B
#�t�q�k�́h��΃p�X�h�ł��肢�v���܂��B
#
#�i��j
#$formhtmlurl = 'http://www.we-box.com/cgi/rfmsap1.html';
#

$formhtmlurl = '';

#�����M�҂̏ڍ׏������[���ɕ\�����遄  ��Ver 2.10�V��
#���M�������̂h�o�A�h���X�Ȃǂ̏������[���ɕ\�����邩�ǂ����̃t���O�ł��B
#���[���e���v���[�g�@�\�������p�̏ꍇ�́A���̃t���O�͌��ʂ���܂���B
#�i�ʓr <!-- senderinfo -->�^�O�����[���e���v���[�g�ɓ���Ă��������B�j
#�O�E�E�E��\���@�P�E�E�E�\��

$senderinfo = 1;


#�����M�҂ɃR�s�[���[���𑗂邩�ǂ����̃t���O��  ��Ver 2.11�V��
#���M�������ɃR�s�[���[���𑗂邩�ǂ����̃t���O�ł��B
#���M�E���e�җp�e���v���[�g�������p�̏ꍇ�́A���̃t���O�͌��ʂ���܂���B
#�O�E�E�E����Ȃ��@�P�E�E�E����

$copymail = 1;

#�S�S�V�s�ȍ~�ɂ��A�C�����ځi���M�҂̖��O�Ń��[���𑗂邩�ǂ����j���������܂��B
#�X�Ȃ�J�X�^�}�C�Y�������߂̕��́A���񂲗��������B

#----------------------------------------------------------------------------
#�ύX���ځA�����܂ŁB
#
#����ȍ~�͉��������݂鎞�ȊO�ύX���Ȃ��ŉ������B
#�Ȃ��A�����̍ۂ͎��ȐӔC�ɂĂ��肢�v���܂��B
#�i�����̍ۂ̃A�h�o�C�X�͒v���܂��̂ŁA���C�y�ɂ����k�������B�j
#-----------------------------------------------------------------------------

#�ϐ��̏�����

local($ctime,$sdata,$default_checkhtml,$default_errorhtml,$Encoding,$CharSet,$viewall,$source_of_mail);
local($mode,$i,$ref,$uri,$let_miss,$errortype);#my
#local(@data);
local(%in,%cookie,$tipad,$thost,$rfmuser);

$rfmuser = 'rfmliteuser';
$name[0] = '���[���̑薼';
$need[0] = 1; #���[���薼�͕K�{�I�I
$Encoding = 'sjis';#�����R�[�h�B
$CharSet = 'shift_jis';#�����R�[�h�B�\���p�ł��B
$ctime = time;

$copyright = '�ERAGE FORM MAIL Lite Version 1.00 Copyright(C) 2000,2001 By <a href="http://www.we-box.com/" target="_top">WE-BOX</a>';
#���쌠�\���ł��B�������ύX�����ꍇ�̓X�N���v�g�̎g�p��F�߂܂���B

require 'r_util.pl';#�ėp�T�u���[�`���̏���
require 'jcode.pl';#���{�ꏈ�����[�`���̏���

&defhtml();#�f�t�H���g�̂g�s�l�k��ǂݍ���
&parseinput($Encoding);#��荞��
$mode = $in{'mode'};
&getlog();#���M�҃��O����

#�O�����p�`�F�b�N
$ref = $ENV{'HTTP_REFERER'};
$uri = $ENV{'REQUEST_URI'};
$ref =~ s/%7E/~/ig;
$uri =~ s/%7E/~/ig;
if ($formhtmlurl && ( ($ENV{'REQUEST_METHOD'} !~ /POST/i) || ($ref !~ /$formhtmlurl/i && !$mode) || ($ref !~ /$formhtmlurl/i && !$chk_skip) || ($ref !~ /$uri/i && $mode eq 'post') ) ) {
	&o_g_illgal('�O������̗��p�͂ł��܂���','���߂�ꂽ�t�H�[�����o�R���Ȃ��A�s���ȊO������̗��p�͂ł��܂���B<br>���߂�ꂽ�t�H�[�����瑗�M���ĉ������B',0);
}
#�f�[�^�`�F�b�J�p�ɁA�t�H�[�����珑�����񂾓��e����荞�ށB
for ($i=1;$i<=$n_of_subject+1;$i++) {
    $data[$i] = &coding_fbd($in{"data$i"});
}

#���[���A�h���X����荞��
$mailcc = $in{'mailcc'};

#�薼����荞��
$data[0] = $in{'data0'} if ($in{'data0'});

#���e�̃`�F�b�N
if (&posttimeparam()) {
    &o_g_illgal('P A C I F I C A____________________�G���[�I','��莞�ԑ҂��Ă���ēx���M���Ă��������B',0);
}

#���M���[�h���ǂ����m�F
&posting() if ($mode eq 'post');

#���[���A�h���X�̌`���m�F
if ($mailcc && $mailcc !~ /^[\w\+\-\.]+@[\w\+\-]+\.[\w\+\.\-]+$/) {
    &o_g_illgal('P A C I F I C A____________________�G���[�I',"���͂��ꂽ���[���A�h���X�ɊԈႢ������܂��B<br>���e���m�F���Ă���A������x��蒼���Ă��������B",0);
}

#�m�F��ʂ̕`��Ɠ��e�m�F
$let_miss = &ch_post();
if ($let_miss) {&o_g_illgal('P A C I F I C A____________________�G���[�I',$let_miss,1);}
&posting() if (!$chk_skip);
$errortype = "P A C I F I C A____________________���e�m�F";
print "Content-type: text/html\n\n";
#�f�t�H���g�p�̊m�F��ʂ����
$viewall = "<table border=1 cellpadding=5 cellspacing=0 width=400 bordercolor=\"$Hbco\">";
$viewall.= "<tr><th bgcolor=\"$Sjco\">����</td><th bgcolor=\"$Ctco\">���e</td></tr>\n";
for ($i=0;$i<@data-1;$i++) {
    $viewall .= "<tr><td bgcolor=\"$Sjco\">$name[$i]</td><td bgcolor=\"$Ctco\">$data[$i]</td></tr>\n";
}
if ($mailcc) {
    $viewall .= "<tr><td bgcolor=\"$Sjco\">���[���A�h���X</td><td bgcolor=\"$Ctco\">$mailcc</td></tr>\n";
}
$viewall .= "</table>\n";

#���M�p�̃��[���\�[�X
$source_of_mail = "<input type=hidden name=mode value=post>\n";
for ($i=0;$i<@data;$i++) {
    $source_of_mail .= "<input type=hidden name=data$i value=\"$data[$i]\">\n";
}
$source_of_mail .= "<input type=hidden name=mailcc value=\"$mailcc\">\n";

#�m�F��ʂ�\�����ďI���
print &tranceskin($checkhtml,$default_checkhtml);
exit(0);

#�G���[����
sub o_g_illgal {
	local($errortype,$errorcontent,$et_sub) =@_;
	print "Content-type: text/html\n\n";
	if ($et_sub) {
		$dealwitherror = '�L�����ꂪ����܂��B�i�K�{�j�Ə����ꂽ���ڂ͕K�����L�����������B<br><br><a href="javascript:history.back();">B A C K</a>';
	} else {
		$dealwitherror = '���[�����M�Ɏ��s���܂����B�G���[���e���悭���ǂ݂ɂȂ��āA�ēx���������������B<br><br><a href="javascript:history.back();">B A C K</a>';
	}
	print &tranceskin($errorhtml,$default_errorhtml);
	exit(0);
}

#���[�����M����
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
'���M����        �@  : '.$cttime."\n".
'�z�X�g��            : '.$thost."\n".
'�h�o�A�h���X�@�@�@�@: '.$tipad."\n".
'���p�u���E�U        : '.$agent."\n".
'�v�����ꂽ���\�b�h�@: '.$ENV{'REQUEST_METHOD'}."\n".
'�X�N���v�g���E�t�q�k: '.$ENV{'SCRIPT_NAME'}."\n".
'�Q�ƌ��t�q�k     �@ : '.$ENV{'HTTP_REFERER'}."\n".
'�T�[�o�̖��O    �@  : '.$ENV{'SERVER_NAME'}."\n".
'�T�[�o�[�̃v���g�R��: '.$ENV{'SERVER_PROTOCOL'}."\n".
'�T�[�o�̃|�[�g�ԍ��@: '.$ENV{'SERVER_PORT'}."\n";

#�X�Ȃ�ݒ莖��
#�ȉ��̂Q�s�́u$logfrom�v�Ɓu$Owner�v���A
#�t�H�[���Ŗ��O���L��������ۂɎw�肵���f�[�^�[�ԍ��ɂ��������ďC������ƁA
#���M�҂̋L���������O�Ń��[��������܂��B
#
#��{�́A
#
# $p_lf = &e_base64("$data[�i�f�[�^�[�ԍ��j]");
#
#
#�Ⴆ�΁A���O�̂Ƃ����<input type="text" name="data2">�Ƃ����ꍇ�A
#
# $p_lf = &e_base64("$data[2]");
#
#�ƁA�ύX���Ă��������B

	$p_lf = &e_base64("$data[2]");

#�w�b�_���������
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

	#���M�揈��
	@sendto = split(/,/,$mailto);
	$mailto = shift(@sendto);
	foreach $tmp (@sendto) {
		$co_mailto .= "Cc: $tmp\n";
	}
	#�R�s�[���[������
	$cc1 = '';
	$cc1 = "From: $p_Ow<$Ownermail>\nReply-To: $p_Ow<$Ownermail>\n" if ($send_bcc);
	
	#�{�������
	if (!$mailformat) {
		$mailcontent .= $mailheader;
		$mailcontent .= "\n\n";
		for ($i=1;$i<@data-1;$i++) {
    		$mailcontent .="$name[$i]\n$data[$i]\n\n";
		}
		if ($mailcc) {
			$mailcontent .= '����̃��[���A�h���X'."\n$mailcc\n\n";
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
	
	#�w�b�_�Ɩ{������������
	$mailcontent2 = $mailcontent if (!$mailformat2);
	$mailcontent  = "To: $p_Ow<$mailto>\n$co_mailto"."From: $p_lf<$post_from>\nReply-To: $p_lf<$post_from>\n".$mailheadinfo."\n".$mailcontent;
	$mailcontent2 = "To: $mailcc\n$cc1".$mailheadinfo."\n".$mailcontent2 if ($copymail);

	#���[���𑗂�
	&jcode'convert(*mailcontent,'jis');
	open (MAIL, "| $mailpass -t");
#or die "���[�����M���s\n";
	print MAIL $mailcontent;
	close (MAIL);

	if ($copymail) {
		&jcode'convert(*mailcontent2,'jis');
		open (MAIL, "| $mailpass -t");
	#or die "���[�����M���s\n";
		print MAIL $mailcontent2;
		close (MAIL);
	}
	#�N�b�L�[�ɍđ��M�h�~�p�̃f�[�^�[����������ł���
	undef %cookie;
	$cookie{'lastposttime'} = $ctime;
	&put_Cookie($rfmuser,30);
	
	#���M�I����ʕ\��
    print "Location: $thankshtmlurl\n\n" if ($thankshtmlurl);
	print "Content-type: text/html\n\n";
	$errortype = "P A C I F I C A____________________���M����";
	$ts_out =~ s/<!-- errorcontent -->/$errorcontent/gi;
	$ts_out =~ s/<!-- dealwitherror -->/$dealwitherror/gi;
	$dealwitherror = $notice2;
	$errorcontent = "<a href=\"$homeurl\"><b>B A C K</b></a>";
	print &tranceskin('',$default_errorhtml);
#print "<form><textarea cols=80 rows=10>$mailcontent</textarea></form>";#�f�o�b�O
#print "<form><textarea cols=80 rows=10>$mailcontent2</textarea></form>";#�f�o�b�O
	exit(0);
}

#�X�L���ϊ����[�`��
sub tranceskin {
	local ($ts_file,$ts_out) = @_;#my
	local ($i,$ownerinfo);#my
	$ts_out = &loadskin($ts_file) if ($ts_file);
	#���ځ��L�����e�̒u������
	for ($i=0;$i<=$n_of_subject+1;$i++) {
		$ts_out =~ s/<!-- data$i -->/$data[$i]/gi;
		$ts_out =~ s/<!-- name$i -->/$name[$i]/gi;
	}
	$ts_out =~ s/<!-- mailcc -->/$mailcc/gi;
	#�w�b�_�����t�b�_�̕��̒u������
	$ts_out =~ s/<!-- header -->/$mailheader/gi;
	$ts_out =~ s/<!-- fooder -->/$mailfooder/gi;
	#�G���[���ƁA�G���[���e�̒u������
	$ts_out =~ s/<!-- error -->/$errortype/gi;
	$ts_out =~ s/<!-- errorcontent -->/$errorcontent/gi;
	$ts_out =~ s/<!-- dealwitherror -->/$dealwitherror/gi;
	#�m�F��ʂ��瑗�M��ʂɁA���������e��n�����߂̋L��
	$ts_out =~ s/<!-- mailcontent -->/$source_of_mail/gi;
	#�e�[�u�����g���āA��C�Ɋm�F���e��\�����邽�߂̋L��
	$ts_out =~ s/<!-- viewall -->/$viewall/gi;
	#���쌠�\���ƊǗ��ҕ\���E���e�ҏ��\��
	$ownerinfo = "<a href=\"mailto:$Ownermail\">$Owner</a>";
	$ts_out =~ s/<!-- ownerinfo -->/$ownerinfo/gi if ($Ow_blank);
	$ts_out =~ s/<!-- copyright -->/$copyright/gi;
	$ts_out =~ s/<!-- senderinfo -->/$sendinfo/gi;
	return $ts_out;
}

#�\���̂��߂̕����ϊ����[�`��
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
    $string =~ s/<br>/\n/g;#���g���̋@��ɂ���ĕύX�肢�܂�
	$string =~ s/&amp;/&/g;
	$string =~ s/&quot;/"/g;
	$string =~ s/&lt;/</g;
	$string =~ s/&gt;/>/g;
	$string =~ s/&#44;/,/g;
    return $string;
}

#�G���[���e�������[�`��

sub ch_post {
    local($i,$cp_out);#my
    for ($i=0;$i<@data-1;$i++) {
        if ($need[$i] && !$data[$i]) {
        $cp_out .= $itempartion.'�m'.$name[$i].'�n';
        }
    }
    if ($needcc && !$mailcc) {
        $cp_out .= $itempartion.'�m���[���A�h���X�n';
    }
return $cp_out;
}

#���d���e�h�~�̂��߂̃��[�`��

#���O�����
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

#���O��ǂ�
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

#���Ԕ���
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

#�f�t�H���g�̂g�s�l�k���e

sub defhtml {

local($dh_tco,$dh_lco,$dh_bgc,$htmlheader,$headermc,$foodermc);#my
$dh_tco =$Body;
$dh_lco =$Body;
$dh_bgc =$Body;
$dh_tco =~ s/.+TEXT="(.......)".+/$1/i;
$dh_lco =~ s/.+ LINK="(.......)".+/$1/i;
$dh_bgc =~ s/.+BGCOLOR="(.......)".+/$1/i;

#�X�^�C���V�[�g�L�q
$htmlheader = <<"END_OF_NT";
END_OF_NT

#�w�b�_�����}�N��
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

#�t�b�_�����}�N��
$foodermc = <<"END_OF_NT";
END_OF_NT

#�m�F��ʗp�̂g�s�l�k
$default_checkhtml = <<"END_OF_NT";
$headermc
<table width=$width><tr><th bgcolor=$Hbco>
</td></tr>
<tr><td>
<b><font color="#CC0000">���L�̓��e�ő��M���܂��B������x���m�F���������B</font></b><br><br>
<!-- viewall -->
<br>
<table><tr><td>
<form action=$bdurl method=POST>
<!-- mailcontent -->
<input type=submit value="�@���M�@"></form>
</td><td>
<input type=submit name value="�@�߂�@" onclick="JavaScript:history.back();"></p>
</td></tr></table>
</td></tr></table></div>
</body></html>
END_OF_NT

#�G���[���e�̂g�s�l�k
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
