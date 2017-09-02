#!D:\Dwimperl\perl\bin\perl.exe

use strict;
use warnings;
use Data::Dumper;
use CGI;
use CGI qw(:cgi-lib :escapeHTML :unescapeHTML);
use CGI::Carp qw(fatalsToBrowser);
#use CGI qw( :standart);
use vars qw(%in);
$|=1;
ReadParse();

use File::Basename qw(dirname);
use lib dirname(__FILE__).'/Utils/';
use Utils::CGI::Session;

my $sess = CGI::Session->new("driver:file", undef, {Directory=>'tmp'})
    or die CGI::Session->errstr();
my $cgi = CGI->new();
my $sid=$sess->id();
my $cookie=$cgi->cookie(CGISESSID => $sess->id);
print $cgi->header( -cookie=>$cookie );


$sess->param('name' => 'Petia');
$sess->param('email'=>'petia@mail.com');
my $name = $sess->param('name');
print 'Hello! '.$name.'!<br>';
print '<a href="test.cgi">LINK</a>'