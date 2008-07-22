%define name	libtubo
%define lib_major 1
%define lib_name	%mklibname tubo %{lib_major}
%define version 4.5.0
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Interprocess communication used by xffm
Version: 	%{version}
Release: 	%{release}

Source:		http://downloads.sourceforge.net/xffm/%{name}-%{version}.tar.bz2
URL:		http://xffm.sf.net
License:	GPL
Group:		Utilities
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
Provides:	%{name} = %{version}-%{release}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with libtubo.

%package -n 	%{lib_name}-devel
Summary:	Development tools for interprocess communication
Group:		Development/C
Requires:	%{lib_name} = %{version}-%{release} glib2-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	tubo-devel = %{version}-%{release}

%description -n %{lib_name}-devel
The libtubo-devel package contains the header files and libraries
necessary for developing programs using libtubo.

%prep
%setup -q

%build
aclocal -I /usr/share/xfce4/dev-tools/m4macros -I ./m4
autoconf
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING* ChangeLog NEWS* README*
%{_libdir}/libtubo.so.*

%files -n %{lib_name}-devel
%{_includedir}/xffm/tubo.h
%{_libdir}/libtubo.a
%{_libdir}/libtubo.so
%{_libdir}/libtubo.la
%{_libdir}/pkgconfig/%{name}.pc


