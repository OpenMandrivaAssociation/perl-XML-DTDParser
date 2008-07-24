%define module	XML-DTDParser
%define name	perl-%{module}
%define version	2.01
%define	release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Quick and dirty DTD parser
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

%description
This perl module parses a DTD file and creates a data structure containing info
about all tags, their allowed parameters, children, parents, optionality etc.
etc. etc.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*

