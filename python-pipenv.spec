# Created by pyp2rpm-3.2.2
%global pypi_name pipenv

Name:           python-%{pypi_name}
Version:        3.5.6
Release:        1%{?dist}
Summary:        Sacred Marriage of Pipfile, Pip, & Virtualenv

License:        MIT
URL:            https://github.com/kennethreitz/pipenv
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pipenv: Sacred Marriage of Pipfile, Pip, & Virtualenv **Pipenv** is an
experimental project that aims to bring the best of all packaging worlds to the
Python world. It harnesses Pipfile < pip < and virtualenv < into one single
toolchain. It features very pretty terminal colors.It automatically creates and
manages a virtualenv for your projects, as well as adds/removes packages from
your...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-pexpect
Requires:       python-virtualenv
Requires:       python-pew >= 0.1.26
Requires:       python-pip
Requires:       python-setuptools
Requires:       python2-pexpect
%description -n python2-%{pypi_name}
Pipenv: Sacred Marriage of Pipfile, Pip, & Virtualenv **Pipenv** is an
experimental project that aims to bring the best of all packaging worlds to the
Python world. It harnesses Pipfile < pip < and virtualenv < into one single
toolchain. It features very pretty terminal colors.It automatically creates and
manages a virtualenv for your projects, as well as adds/removes packages from
your...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-pexpect
Requires:       python3-virtualenv
Requires:       python3-pew >= 0.1.26
Requires:       python3-pip
Requires:       python3-setuptools
Requires:       python3-pexpect
%description -n python3-%{pypi_name}
Pipenv: Sacred Marriage of Pipfile, Pip, & Virtualenv **Pipenv** is an
experimental project that aims to bring the best of all packaging worlds to the
Python world. It harnesses Pipfile < pip < and virtualenv < into one single
toolchain. It features very pretty terminal colors.It automatically creates and
manages a virtualenv for your projects, as well as adds/removes packages from
your...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

# Unbundle packages under the vendor. We replace these with symlinks to system libs.
rm -rf build/lib/pipenv/vendor/pexpect

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
cp %{buildroot}/%{_bindir}/pipenv %{buildroot}/%{_bindir}/pipenv-%{python3_version}
ln -s %{_bindir}/pipenv-%{python3_version} %{buildroot}/%{_bindir}/pipenv-3
ln -s ../../pexpect %{buildroot}/%{python3_sitelib}/pipenv/vendor/pexpect

%py2_install
cp %{buildroot}/%{_bindir}/pipenv %{buildroot}/%{_bindir}/pipenv-%{python2_version}
ln -s %{_bindir}/pipenv-%{python2_version} %{buildroot}/%{_bindir}/pipenv-2
ln -s ../../pexpect %{buildroot}/%{python2_sitelib}/pipenv/vendor/pexpect

%check


%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/pipenv
%{_bindir}/pipenv-2
%{_bindir}/pipenv-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/pipenv-3
%{_bindir}/pipenv-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Apr 20 2017 Jun Aruga <jaruga@redhat.com> - 3.5.6-1
- Initial package.
