#!D:\Dwimperl\perl\bin\perl.exe

use strict;
use warnings;
use Data::Dumper;
use CGI qw(:cgi-lib :escapeHTML :unescapeHTML);
use CGI::Carp qw(fatalsToBrowser);
use vars qw(%in);
$|=1;
ReadParse();

use File::Basename qw(dirname);
use lib dirname(__FILE__).'/Utils/';
use Utils::CGI::Session;



my $cgi = CGI->new();
my $sid = $cgi->cookie("CGISESSID") || undef;
my $sess = new CGI::Session(undef, $sid, {Directory=>'tmp'});
print "Content-type: text/html; charset=utf-8\n\n";


print "Hello ".$sess->param('name').'<br>';
print "Your email is: ".$sess->param('email').'<br>';
print 'Session id: '.$sess->id().'<br>';


print '<a href="?page=clear">Logout</a>';

print '<pre>'.Dumper(\%in).'</pre>';
my $page = %in->{'page'};
if ($page eq 'clear'){
    $sess->delete();
    print '<hr>Logout - clear session!!!';
}