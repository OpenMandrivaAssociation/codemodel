%_javapackages_macros
Name:         codemodel
Version:      2.6
Release:      10.0%{?dist}
Summary:      Java library for code generators
License:      CDDL and GPLv2
URL:          http://codemodel.java.net
# svn export https://svn.java.net/svn/codemodel~svn/tags/codemodel-project-2.6/ codemodel-2.6
# tar -zcvf codemodel-2.6.tar.gz codemodel-2.6
Source0:      %{name}-%{version}.tar.gz
# Remove the dependency on istack-commons (otherwise it will be a
# recursive dependency with the upcoming changes to that package):
Patch0:       %{name}-remove-istack-commons-dependency.patch

BuildArch:     noarch

BuildRequires: java-devel

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: mvn(net.java:jvnet-parent)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(junit:junit)

Requires:      mvn(net.java:jvnet-parent)


%description
CodeModel is a Java library for code generators; it provides a way to
generate Java programs in a way much nicer than PrintStream.println().
This project is a spin-off from the JAXB RI for its schema compiler
to generate Java source files.

%package javadoc
Summary: Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep

# Unpack and patch the original source:
%setup -q
%patch0 -p1

# Remove bundled jar files:
find . -name '*.jar' -print -delete

%build

%mvn_file :%{name} %{name}
%mvn_file :%{name}-annotation-compiler %{name}-annotation-compiler
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.html
