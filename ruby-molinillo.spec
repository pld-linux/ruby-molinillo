%define	pkgname	molinillo
Summary:	Provides support for dependency resolution
Summary(pl.UTF-8):	Obsługa rozwiązywania zależności
Name:		ruby-%{pkgname}
Version:	0.6.5
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	920426fc9bbfbe101b4a5a0559a5ae43
URL:		https://github.com/CocoaPods/Molinillo
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
# not used when packaging from .gem
#BuildRequires:	ruby-bundler >= 1.5
#BuildRequires:	ruby-bundler < 2
#BuildRequires:	ruby-rake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides support for dependency resolution.

%description -l pl.UTF-8
Moduł zapewniający obsługę rozwiązywania zależności.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ARCHITECTURE.md CHANGELOG.md LICENSE README.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
