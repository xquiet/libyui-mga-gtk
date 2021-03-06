%define         git          5ded95a
%define         gitdate      20131106
%define         major        5
%define         libname      %mklibname yui %{major}-mga-gtk
%define         develname    %mklibname -d yui-mga-gtk

Name:           libyui-mga-gtk
Version:        1.0.0
Release:        %mkrel -c git%{gitdate} 1
Summary:        UI abstraction library - Gtk plugin
License:        LGPLv2+
Group:          System/Libraries
Url:            git@bitbucket.org:_pmat_/libyui-mga-gtk.git
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:    yui-devel
BuildRequires:    %{_lib}yui-gtk-devel
BuildRequires:    %{_lib}yui-mga-devel
BuildRequires:    libgtk+3.0-devel
BuildRequires:    cmake
BuildRequires:    boost-devel
BuildRequires:    doxygen
BuildRequires:    texlive
BuildRequires:    ghostscript
Requires:         libyui
Requires:         libyui-mga
Requires:         libyui-gtk

%description
%{summary}

#-----------------------------------------------------------------------

%package -n %libname
Summary:        %{summary}
Group:          System/Libraries
Requires:       libyui
Provides:       %{name} = %{version}-%{release}

%description -n %libname
This package contains the library needed to run programs
dynamically linked with libyui-mga-gtk.

%files -n %libname
%doc COPYING*
%{_libdir}/yui/lib*.so.*


#-----------------------------------------------------------------------

%package -n %develname
Summary:        %{summary} header files
Group:          Development/Other
Requires:       libyui-devel
Requires:       %{name} = %{version}-%{release}


%description -n %develname
This package provides headers files for libyui-mga-gtk development.

%files -n %develname
%{_includedir}/yui
%{_libdir}/yui/lib*.so
%{_libdir}/pkgconfig/libyui-mga-gtk.pc
%{_libdir}/cmake/libyui-mga-gtk
%doc %{_docdir}/libyui-mga-gtk%{major}

#-----------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%apply_patches

%build
./bootstrap.sh
%cmake -DPREFIX=%{_prefix}  \
       -DDOC_DIR=%{_docdir} \
       -DLIB_DIR=%{_lib}    \
       -DINSTALL_DOCS=yes


%make docs

%install
rm -rf %{buildroot}
%makeinstall_std -C build
find "%{buildroot}" -name "*.la" -delete
