%define upstream_name    MooseX-Storage
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A custom meta-attribute-trait to bypass serialization
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::TempDir)

BuildArch:	noarch

%description
MooseX::Storage is a serialization framework for Moose, it provides a very
flexible and highly pluggable way to serialize Moose classes to a number of
different formats and styles.

Important Note
    This is still an early release of this module, so use with caution.
    It's outward facing serialization API should be considered stable, but
    I still reserve the right to make tweaks if I need too. Anything beyond
    the basic pack/unpack, freeze/thaw and load/store should not be relied
    on.

Levels of Serialization
    There are 3 levels to the serialization, each of which builds upon the
    other and each of which can be customized to the specific needs of your
    class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 662127
- update to new version 0.30

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.290.0-2
+ Revision: 656945
- rebuild for updated spec-helper

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 601937
- update to new version 0.29

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 596738
- adding missing buildrequires
- update to 0.28

* Fri Aug 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.270.0-1mdv2011.0
+ Revision: 573482
- import perl-MooseX-Storage

