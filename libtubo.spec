%define oname tubo
%define lib_major 0
%define lib_name	%mklibname %{oname} %{lib_major}
%define dev_name	%mklibname %{oname} -d

Name:		libtubo
Summary:	Interprocess communication used by xffm
Version:	4.7.6
Release:	2

Source0:	http://downloads.sourceforge.net/project/xffm/libtubo/%{oname}-%{version}.tar.gz
Patch0:		tubo-4.7.6-rosa-linkage.patch
Patch1:		tubo-4.7.6-rosa-no_rpath.patch
URL:		https://xffm.sf.net
License:	GPLv2+
Group:		System/Libraries
BuildRequires:	xfce-dev-tools
BuildRequires:	autoconf2.5
BuildRequires:	automake1.9
BuildRequires:	intltool
BuildRequires:	glib-gettextize
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc

%description
The Libtubo library is small and simple function set to enable a process 
to run any other process in the background and communicate via 
the stdout, stderr and stdin file descriptors.

%package -n	%{lib_name}
Summary:	A library of functions for interprocess communication
Group:		System/Libraries
Provides:	%{name} = %{EVRD}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with libtubo.

%package -n 	%{dev_name}
Summary:	Development tools for interprocess communication
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	tubo-devel = %{EVRD}

%description -n %{dev_name}
The libtubo-devel package contains the header files and libraries
necessary for developing programs using libtubo.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1
%patch1 -p1

%build
aclocal -I /usr/share/xfce4/dev-tools/m4macros -I ./m4
autoreconf
%configure2_5x
%make

%install
%makeinstall

%files -n %{lib_name}
%doc AUTHORS COPYING* ChangeLog NEWS* README*
%{_libdir}/libtubo.so.%{lib_major}*

%files -n %{dev_name}
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/tubo.h
%{_libdir}/libtubo.so
%{_libdir}/pkgconfig/%{oname}.pc


%changelog
* Tue Jan 09 2007 Crispin Boylan <crisb@mandriva.org> 4.5.0-1mdv2007.1
+ Revision: 106586
- Fix provides
- BuildRequires gtk-doc
- BuildRequires glib2
- BuildRequires pkgconfig
- First mandriva version
- Create libtubo

