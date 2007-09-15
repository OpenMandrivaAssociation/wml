%define version 2.0.9
%define release %mkrel 13
%define name wml

Summary:   Website META Language
Name:      %{name}
Version:   %{version}
Release:   %{release}
License: GPL
Buildroot: %{_tmppath}/%{name}-buildroot
Group:     Publishing
Source:    %{name}-%{version}.tar.bz2
Patch0:     wml-2.0.9-require.patch.bz2
Patch1:     wml-2.0.9-pathconvert.patch.bz2
Patch2:     wml-2.0.9-perllibs.patch.bz2
Patch3:     wml-2.0.9-gcc4.patch.bz2
Url:       http://www.engelschall.com/sw/wml
BuildRequires: perl-devel
BuildRequires: libncurses-devel
# Please do not ever link this with an old db version than the current system db version
# libperl uses {get,set}pw*() functions which might bring in the system db version via nss,
# and lead to unexpected crashes
# BuildRequires: db2-devel, libgdbm-devel

BuildRequires: perl(Getopt::Long) >= 2.16
BuildRequires: perl-Bit-Vector >= 5.2
BuildRequires: perl(File::Spec)
BuildRequires: perl(Image::Size) >= 2.6
BuildRequires: perl(IO::File) >= 1.07
BuildRequires: perl(Term::ReadKey) >= 2.11

# why does not autorequires catch those???
Requires: perl(Getopt::Long) >= 2.16
Requires: perl(Bit::Vector) >= 5.2
Requires: perl(File::Spec)
Requires: perl(Image::Size) >= 2.6
Requires: perl(IO::File) >= 1.07
Requires: perl(Term::ReadKey) >= 2.11


# do not provide/require private perl modules
%define _requires_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)
%define _provides_exceptions GD.so\\|perl(HTML::Clean)\\|perl(WML::GD)

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
%patch3 -p1 -b .gcc4

%build
( cd wml_backend/p3_eperl; autoconf )

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%_prefix --libdir=%_libdir --with-openworld

%make

make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall libdir=$RPM_BUILD_ROOT%{_libdir}/wml

#clean perl files (stolen from spec-helper)
d=$RPM_BUILD_ROOT%{_libdir}/wml
find $d -name ".packlist" | xargs rm -f
for i in $(find $d -name "*.bs"); do
    if [ -s $i ]; then
      echo "non empty *.bs file, please mail pixel@mandriva.com about this!"
    else
      rm -f $i
    fi
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ANNOUNCE BUGREPORT ChangeLog COPYING COPYRIGHT COPYRIGHT.OTHER CREDITS 
%doc NEWS README SUPPORT VERSION VERSION.HISTORY
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/*/*
