# do not provide/require private perl modules
%define _requires_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)
%define _provides_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)

Summary:	Website META Language
Name:		wml
Version:	2.0.11
Release:	%mkrel 1
License:	GPL
Group:		Publishing
URL:		http://www.engelschall.com/sw/wml
Source:		http://thewml.org/distrib/%{name}-%{version}.tar.gz
Patch0:		wml-2.0.9-require.patch
Patch1:		wml-pathconvert.diff
Patch2:		wml-2.0.9-perllibs.patch
Patch3:		wml-LD_RUN_PATH.diff
Patch4:		wml-external_pcre_libs.diff
BuildRequires:	ncurses-devel
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	perl-devel
BuildRequires:	gettext-devel
BuildRequires:	lynx
# Please do not ever link this with an old db version than the current system db version
# libperl uses {get,set}pw*() functions which might bring in the system db version via nss,
# and lead to unexpected crashes
# BuildRequires: db2-devel, libgdbm-devel
BuildRequires:	perl-Bit-Vector >= 5.2
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Getopt::Long) >= 2.16
BuildRequires:	perl(Image::Size) >= 2.6
BuildRequires:	perl(IO::File) >= 1.07
BuildRequires:	perl(Term::ReadKey) >= 2.11
# why does not autorequires catch those???
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
based source tree and runs out-of-the-box on all major Unix derivates.
It can be used free of charge both in educational and commercial
environments.

%prep

%setup -q
%patch0 -p1 -b .require
%patch1 -p1 -b .pathconvert
%patch2 -p1 -b .perllibs
%patch3 -p0 -b .LD_RUN_PATH
%patch4 -p1 -b .external_pcre_libs

find -type d -name "autom4te.cache" | xargs rm -rf 

find -type f -name "Makefile*" | xargs perl -pi -e "s|\\$\(prefix\)/lib\\$\(libsubdir\)|\\$\(prefix\)/%{_lib}\\$\(libsubdir\)|g"
perl -pi -e "s|lib=\"lib|lib=\"%{_lib}|g" wml_test/Makefile.in

%build
pushd wml_backend/p3_eperl
    autoconf
popd

pushd wml_backend/p2_mp4h
    libtoolize --automake -c -f; aclocal; automake -a -c; autoheader; autoconf
popd

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --with-openworld

%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall libdir=%{buildroot}%{_libdir}/wml

#clean perl files (stolen from spec-helper)
d=%{buildroot}%{_libdir}/wml
find $d -name ".packlist" | xargs rm -f
for i in $(find $d -name "*.bs"); do
    if [ -s $i ]; then
      echo "non empty *.bs file, please mail pixel@mandriva.com about this!"
    else
      rm -f $i
    fi
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ANNOUNCE BUGREPORT ChangeLog COPYING COPYRIGHT COPYRIGHT.OTHER CREDITS 
%doc NEWS README SUPPORT VERSION VERSION.HISTORY
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*
