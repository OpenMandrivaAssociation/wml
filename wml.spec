# do not provide/require private perl modules
%if %{_use_internal_dependency_generator}
%define __noautoreq 'GD\\.so|perl\\(HTML::Clean\\)|perl\\(WML::GD\\)'
%define __noautoprov 'GD\\.so|perl\\(HTML::Clean\\)|perl\\(WML::GD\\)'
%else
%define _requires_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)
%define _provides_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)
%endif

Summary:	Website META Language
Name:		wml
Version:	2.4.1
Release:	2
License:	GPLv2+
Group:		Publishing
URL:		http://thewml.org/
Source:		https://bitbucket.org/shlomif/website-meta-language/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	libtool
BuildRequires:	libltdl-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-devel
# (tpg) use system version not the pulled in here
#BuildRequires:	db-devel
# (crisb) doesnt seem to pull in the db-devel package so spec here
BuildRequires:	db53-devel
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	lynx
BuildRequires:	perl-Bit-Vector >= 5.2
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(GD)
BuildRequires:	perl(Getopt::Long) >= 2.16
BuildRequires:	perl(HTML::Clean)
BuildRequires:	perl(Image::Size) >= 2.6
BuildRequires:	perl(IO::File) >= 1.07
BuildRequires:	perl(Term::ReadKey) >= 2.11
Requires:	perl(Bit::Vector) >= 5.2
Requires:	perl(File::Spec)
Requires:	perl(Getopt::Long) >= 2.16
Requires:	perl(Image::Size) >= 2.6
Requires:	perl(IO::File) >= 1.07
Requires:	perl(Term::ReadKey) >= 2.11

%description
WML is a free and extensible Webdesigner's off-line HTML generation
toolkit for Unix, distributed under the GNU General Public License
(GPL v2). It is written in ANSI C and Perl 5, build via a GNU Autoconf
based source tree and runs out-of-the-box on all major Unix derivatives.
It can be used free of charge both in educational and commercial
environments.

%prep
%setup -q

%build
%cmake -DLIB_INSTALL_DIR=%{_libdir} -DLOCALE_INSTALL_DIR=%{_datadir}/locale
%make

# TODO : add percent-check once it is working.

%install
%makeinstall_std -C build

%files
%doc ANNOUNCE BUGREPORT ChangeLog COPYING COPYRIGHT COPYRIGHT.OTHER CREDITS 
%doc NEWS README SUPPORT VERSION VERSION.HISTORY
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*
