Summary:	Integrated TeX/LaTeX Environment for the GNOME desktop
Summary(pl.UTF-8):	Zintegrowane środowisko TeXowe/LaTeXowe dla GNOME
Name:		enter-tex
Version:	3.47.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/enter-tex/3.47/%{name}-%{version}.tar.xz
# Source0-md5:	962c377147347ad8d6ca0cc395117bd9
URL:		https://gitlab.gnome.org/swilmet/enter-tex
BuildRequires:	appstream-glib-devel
BuildRequires:	dconf-devel
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.80
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gspell-devel >= 1.8
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libgedit-amtk-devel >= 5.8
BuildRequires:	libgedit-gtksourceview-devel >= 299
BuildRequires:	libgedit-tepl-devel >= 6.11
BuildRequires:	libgee-devel >= 0.10
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.46
BuildRequires:	vala-gspell >= 1.8
BuildRequires:	vala-gtksourceview4 >= 4.0
BuildRequires:	vala-libgee >= 0.10
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.80
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.80
Requires:	gsettings-desktop-schemas
Requires:	gspell >= 1.8
Requires:	gtk+3 >= 3.22
Requires:	hicolor-icon-theme
Requires:	libgedit-amtk >= 5.8
Requires:	libgedit-gtksourceview >= 299
Requires:	libgedit-tepl >= 6.11
Requires:	libgee >= 0.10
Suggests:	latexmk >= 4.31
Obsoletes:	gnome-latex < 3.47
Obsoletes:	latexila < 3.28
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enter TeX is a TeX/LaTeX text editor for the GNOME desktop. It was
previously named LaTeXila and then GNOME LaTeX.

%description -l pl.UTF-8
Enter TeX to edytor tekstu TeX/LaTeX dla środowiska GNOME. Wcześniej
projekt nazywał się LaTeXila, następnie GNOME LaTeX.

%prep
%setup -q

%build
%meson build

# missing proper in-tree dependences, need to build gir first
%ninja_build -C build src/gtex/Gtex-1.gir

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/enter-tex
%{_datadir}/dbus-1/services/org.gnome.enter_tex.service
%{_datadir}/glib-2.0/schemas/org.gnome.enter_tex.gschema.xml
%{_datadir}/enter-tex
%{_datadir}/metainfo/org.gnome.enter_tex.metainfo.xml
%{_desktopdir}/org.gnome.enter_tex.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.enter_tex.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.enter_tex-symbolic.svg
%{_mandir}/man1/enter-tex.1*
%{_gtkdocdir}/enter-tex
