#!/usr/bin/perl
use warnings; use strict;
#This script remove duplicated spectrum from file input. The output 

my %seen; 
my $count = 0; 
my $output;

open STDOUT, '>', "total.norepeat.clustering" or die "Can't create filehandle: $!";
while (  <> ) {
	$_ =~ s/;+/;/g;
	next if ( m/spectrum=(\d+)/ and $seen{$1}++ );
	if ( m/==Cluster==/ ) { 
		open ( $output, ">", "temp".$count++ ) or die $!; 
		select $output;
	}
	$_ =~ s/;+/;/g;
	print;
}
	close STDOUT
