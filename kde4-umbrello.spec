#
# TODO:
# - add man files
#
%define		orgname		umbrello
%define		_state		stable
%define		qtver		4.8.1

Summary:	UML Modeler
Summary(pl.UTF-8):	Modeler UML
Name:		kde4-%{orgname}
Version:	4.12.3
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	5bdfe12fac32ef9992910087e179e7c9
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	hunspell-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdesdk-%{orgname}
Obsoletes:	umbrello
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Umbrello UML Modeller is a UML diagram tool that can support you in
the software development process. Especially during the analysis and
design phases of this process, Umbrello UML Modeller will help you to
get a high quality product. UML can also be used to document your
software designs to help you and your fellow developers.

UML is the diagramming language used to describing such models. You
can represent your ideas in UML using different types of diagrams.
Umbrello UML Modeller 1.2 supports the following types:
- class Diagram
- sequence Diagram
- collaboration Diagram
- use Case Diagram
- state Diagram
- activity Diagram
- component Diagram

%description -l pl.UTF-8
Modeler UML Umbrello to narzędzie do diagramów UML pomagające w
procesie tworzenia oprogramowania. Szczególnie podczas etapów analizy
i projektowania, modeler UML Umbrello może pomóc w uzyskaniu wysokiej
jakości produktu. UML może być używany do dokumentowania projektu
programu, aby pomóc programiście i jego współpracownikom.

UML to język diagramów używany do opisu takich modeli. Można
przedstawiać idee w UML-u przy użyciu różnych rodzajów diagramów.
Modeler UML Umbrello 1.2 obsługuje następujące rodzaje:
 - diagram klas
 - diagram sekwencji
 - diagram współpracy
 - diagram przypadków użycia
 - diagram stanów
 - diagram aktywności
 - diagram składników.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang	%{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/umbrello
%{_datadir}/apps/umbrello
%{_desktopdir}/kde4/umbrello.desktop
%{_iconsdir}/*/*x*/*/umbrello*.*
%{_iconsdir}/*/*/mimetypes/application-x-uml.png
%{_iconsdir}/hicolor/scalable/apps/umbrello.svgz
