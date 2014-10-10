%define upstream_name	 XML-DTDParser
%define upstream_version 2.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Quick and dirty DTD parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This perl module parses a DTD file and creates a data structure containing info
about all tags, their allowed parameters, children, parents, optionality etc.
etc. etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/*
%{_mandir}/*/*


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.10.0-1mdv2010.0
+ Revision: 408233
- rebuild using %%perl_convert_version

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.01-7mdv2009.0
+ Revision: 258837
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.01-6mdv2009.0
+ Revision: 246724
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.01-4mdv2008.1
+ Revision: 136365
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.01-4mdv2008.0
+ Revision: 64820
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 2.01-3mdv2008.0
+ Revision: 23519
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.01-2mdk
- Fix According to perl Policy
	- Source URL
- use mkrel

* Tue Nov 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.01-1mdk
- Initial MDK release.

