# Inject Sec to DevOps
List of Tools...

## Python Ecosystem
### Planning Stage

### Development Stage
<details><summary>`Detect-secrets` (https://github.com/Yelp/detect-secrets)</summary>

detect-secrets is an aptly named module for detecting secrets within a code base.

**Features:**
- There are three components that you can setup, depending on your purposes.
- Client-side Pre-Commit Hook, that alerts developers when they attempt to enter a secret in the code base.
- Server-side Secret Scanning, to periodically scan tracked repositories, and make sure developers didn't accidentally skip the pre-commit check.
- Secrets Baseline, to allow list pre-existing secrets in the repository, so that they won't be continuously caught through scan iterations.
</details>

<details><summary>`Talisman` (https://github.com/thoughtworks/talisman)</summary>

Talisman is a tool that installs a hook to your repository to ensure that potential secrets or sensitive information do not leave the developer's workstation. It validates the outgoing changeset for things that look suspicious - such as potential SSH keys, authorization tokens, private keys, etc.

**Features:**
Installation of Talisman globally does not clobber pre-existing hooks on repositories. Integration with:
- Pre-commit (Linux/Unix)
- Husky (Linux/Unix/Windows)
</details>

<details><summary>`Sonarqube` (https://www.sonarqube.org/)</summary>

SonarQube is an automatic code review tool to detect bugs, vulnerabilities and code smells in your code. It can integrate with your existing workflow to enable continuous code inspection across your project branches and pull requests.

**Features:**

- For 25+ programming languages (Java, JavaScript, Python, GO, PHP, etc.).
- CI/CD integration (Jenkins, Azure DevOps server and many others).
- Fix vulnerabilities that compromise your app.
- Make sure your codebase is clean and maintainable.
</details>

<details><summary>`Confidant` (https://github.com/lyft/confidant)</summary>

Confidant is an open source secret management service that provides user-friendly storage and access to secrets in a secure way, from the developers at Lyft.

**Features:**
- KMS Authentication (Confidant solves the authentication chicken and egg problem by using AWS KMS and IAM to allow IAM roles)
- At-rest encryption of versioned secrets (Confidant stores secrets in an append-only way in DynamoDB)
- A user-friendly web interface for managing secrets
</details>

<details><summary>`Bandit` (https://github.com/PyCQA/bandit)</summary>

Bandit is a tool designed to find common security issues in Python code. To do this Bandit processes each file, builds an AST from it, and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files it generates a report.

**Features:**
- Projects may include a .bandit file that specifies command line arguments that should be supplied for that project. 
- Allows users to write and register extensions for checks and formatters
- Integration wir  pre-commit.
</details>

<details><summary>`Safety` (https://github.com/pyupio/safety)</summary>

Safety CI checks your commits and pull requests on GitHub for dependencies with known security vulnerabilities.
</details>

<details><summary>`AWS Secrets Manager` (https://aws.amazon.com/es/secrets-manager/)</summary>

AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

**Features:**
- Rotate secrets safely.
- Manage access with fine-grained policies.
- Secure and audit secrets centrally.
- Pay as you go ($0.05 per 10,000 API calls).
</details>

<details><summary>`Vault` (https://www.vaultproject.io/)</summary>

Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing.

**Features:**
- Secrets Management (Dynamic Secrets, Secret Storage, Secure Plugins, UI with Cluster Management, etc).
- Data Protection (Encryption as a Service, Transit Backend, etc).
- Identity-based Access (Entities & identity groups, AWS KMS Auto-unseal, etc).
</details>

<details><summary>`OWASP Dependency-Check` (https://www.owasp.org/index.php/OWASP_Dependency_Check)</summary>

Dependency-Check is a software composition analysis utility that identifies project dependencies and checks if there are any known, publicly disclosed, vulnerabilities.

**Features:**
- Dependency-Check is a software composition analysis utility that identifies project dependencies and checks if there are any known, publicly disclosed, vulnerabilities.
- Third party libraries like National Vulnerability Database.
- Common Platform Enumeration (CPE).
- Common Vulnerability and Exposure (CVE).
</details>

<details><summary>`Sonatype` (https://ossindex.sonatype.org/)</summary>

OSS Index is a free service used by developers to identify open source dependencies and determine if there are any known, publicly disclosed, vulnerabilities. OSS Index is based on vulnerability data derived from public sources and does not include human curated intelligence nor expert remediation guidance.

**Features:**
- Identify open source security vulnerabilities across a wide range of components (PyPI, Maven, Bower, NPM, RPM, Debian, etc).
- Integrations open source vulnerability information across your development toolchain with pre-built tools and applications (Audit.js, DevAudit, ossaudit, Sonatype DepShield, etc).
</details>
 
<details><summary>`Snyk` (https://snyk.io/ )</summary>

Snyk helps you use open source and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and much more.

**Features:**
- Snyk can connect directly to the applications you use daily to monitor your projects (Heroku, GitHub, GitLab, AWS Lambda, etc).
- Multi-language support (Python, Goland, PHP, Node.js, Ruby, Java, etc).
</details>

<details><summary>`Clair` (https://github.com/coreos/clair)</summary>

Clair is an open source project for the static analysis of vulnerabilities in application containers (currently including appc and docker). Our goal is to enable a more transparent view of the security of container-based infrastructure. Thus, the project was named Clair after the French term which translates to clear, bright, transparent.

<details><summary>`Anchore Engine` (https://github.com/anchore/anchore-engine)</summary>
The Anchore Engine is an open source project that provides a centralized service for inspection, analysis and certification of container images. The Anchore engine is provided as a Docker container image that can be run standalone, or within an orchestration platform such as Kubernetes, Docker Swarm, Rancher, Amazon ECS, and other container orchestration platforms.

**Features:**
- Helm Chart for installing Anchore Engine in Kubernetes.
- The Open-Source CLI for Anchore Engine.
- Jenkins Plugin for using Anchore Engine in your builds, including results visualizations and reports.
- Anchore Engine pre-built containers.
- Make pod execution decisions based on anchore analysis and policy decisions.
- CircleCI Orb for adding Anchore Engine scanning to your CircleCI builds.
</details>

<details><summary>`Dagda` (https://github.com/eliasgranderubio/dagda)</summary>

Dagda is a tool to perform static analysis of known vulnerabilities, trojans, viruses, malware & other malicious threats in docker images/containers and to monitor the docker daemon and running docker containers for detecting anomalous activities.

**Features:**
Dagda supports multiple Linux base images:
- Red Hat/CentOS/Fedora
- Debian/Ubuntu
- OpenSUSE
- Alpine

Dagda rests on OWASP dependency check + Retire.js for analyzing multiple dependencies from:
- Java
- Python
- JavaScript
- Ruby
- Php
</details>

<details><summary>`Dev-Sec` (https://dev-sec.io/)</summary>

Security + DevOps: Automatic Server Hardening. An excellent resource for automated hardening is a set of open source templates originally developed at Deutsche Telekom. It covers most of the required hardening checks based on multiple standards, which includes Ubuntu Security Features, NSA Guide to Secure Configuration, ArchLinux System Hardening and others.

**Features:**
- Continuous management (this area includes tasks like patch management, attack monitoring, and fixing known vulnerabilities).
- Patch management.
- Attack monitoring (hardening includes a small section of compliance monitoring).
- Vulnerability fixes.
</details>

### Operations Stage
<details><summary>`OWASP ZAP` (https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project)</summary>

The OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers.

**Features:**
- Automated Penetration Testing to Continuous Integration Pipelines.
- Automated Scanner
- Brute Force Scanner
- Web Sockets
- REST API
</details>

<details><summary>`OpenVAS` (http://openvas.org/)</summary>

OpenVAS is a full-featured vulnerability scanner. Its capabilities include unauthenticated testing, authenticated testing, various high level and low level Internet and industrial protocols, performance tuning for large-scale scans and a powerful internal programming language to implement any type of vulnerability test.
</details>

<details><summary>`CCAT` (https://github.com/RhinoSecurityLabs/ccat)</summary>

Cloud Container Attack Tool (CCAT) is a tool for testing security of container environments.
</details>

<details><summary>`Spaghetti` (https://github.com/cyberheartmi9/Spaghetti)</summary>

Spaghetti is an Open Source web application scanner, it is designed to find various default and insecure files, configurations, and misconfigurations. Spaghetti is built on python2.7 and can run on any platform which has a Python environment.
</details>

## JavaScript Ecosystem
### Planning Stage

### Development Stage
`Retire.js` (https://github.com/RetireJS/retire.js)

The goal of Retire.js is to help you detect use of version with known vulnerabilities.

**Features:**

- Command line scanner.
- Burp and OWASP ZAP plugins.
- JavaScript libraries (angularjs, backbone.js, dojo, ember, ExtJS, react, vue.js, ember, etc).
- Node packages.

`OWASP Dependency-Check` (https://www.owasp.org/index.php/OWASP_Dependency_Check)

Dependency-Check is a software composition analysis utility that identifies project dependencies and checks if there are any known, publicly disclosed, vulnerabilities.

**Features:**
- Dependency-Check is a software composition analysis utility that identifies project dependencies and checks if there are any known, publicly disclosed, vulnerabilities.
- Third party libraries like National Vulnerability Database.
- Common Platform Enumeration (CPE).
- Common Vulnerability and Exposure (CVE).
    
`Sonarqube` (https://www.sonarqube.org/)

SonarQube is an automatic code review tool to detect bugs, vulnerabilities and code smells in your code. It can integrate with your existing workflow to enable continuous code inspection across your project branches and pull requests.

**Features:**

- For 25+ programming languages (Java, JavaScript, Python, GO, PHP, etc.).
- CI/CD integration (Jenkins, Azure DevOps server and many others).
- Fix vulnerabilities that compromise your app.
- Make sure your codebase is clean and maintainable.

`AWS Secrets Manager` (https://aws.amazon.com/es/secrets-manager/ )

AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

**Features:**
- Rotate secrets safely.
- Manage access with fine-grained policies.
- Secure and audit secrets centrally.
- Pay as you go ($0.05 per 10,000 API calls).

`Vault` (https://www.vaultproject.io/ )

Vault secures, stores, and tightly controls access to tokens, passwords, certificates, API keys, and other secrets in modern computing.

**Features:**
- Secrets Management (Dynamic Secrets, Secret Storage, Secure Plugins, UI with Cluster Management, etc).
- Data Protection (Encryption as a Service, Transit Backend, etc).
- Identity-based Access (Entities & identity groups, AWS KMS Auto-unseal, etc).

`Sonatype` (https://ossindex.sonatype.org/ )

OSS Index is a free service used by developers to identify open source dependencies and determine if there are any known, publicly disclosed, vulnerabilities. OSS Index is based on vulnerability data derived from public sources and does not include human curated intelligence nor expert remediation guidance.

**Features:**
- Identify open source security vulnerabilities across a wide range of components (PyPI, Maven, Bower, NPM, RPM, Debian, etc).
- Integrations open source vulnerability information across your development toolchain with pre-built tools and applications (Audit.js, DevAudit, ossaudit, Sonatype DepShield, etc).

`Snyk` (https://snyk.io/ )

Snyk helps you use open source and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and much more.

**Features:**
- Snyk can connect directly to the applications you use daily to monitor your projects (Heroku, GitHub, GitLab, AWS Lambda, etc).
- Multi-language support (Python, Goland, PHP, Node.js, Ruby, Java, etc).

`Clair` (https://github.com/coreos/clair)

Clair is an open source project for the static analysis of vulnerabilities in application containers (currently including appc and docker). Our goal is to enable a more transparent view of the security of container-based infrastructure. Thus, the project was named Clair after the French term which translates to clear, bright, transparent.

`Anchore Engine` (https://github.com/anchore/anchore-engine)
The Anchore Engine is an open source project that provides a centralized service for inspection, analysis and certification of container images. The Anchore engine is provided as a Docker container image that can be run standalone, or within an orchestration platform such as Kubernetes, Docker Swarm, Rancher, Amazon ECS, and other container orchestration platforms.

**Features:**
- Helm Chart for installing Anchore Engine in Kubernetes.
- The Open-Source CLI for Anchore Engine.
- Jenkins Plugin for using Anchore Engine in your builds, including results visualizations and reports.
- Anchore Engine pre-built containers.
- Make pod execution decisions based on anchore analysis and policy decisions.
- CircleCI Orb for adding Anchore Engine scanning to your CircleCI builds.

`Dagda` (https://github.com/eliasgranderubio/dagda)

Dagda is a tool to perform static analysis of known vulnerabilities, trojans, viruses, malware & other malicious threats in docker images/containers and to monitor the docker daemon and running docker containers for detecting anomalous activities.

**Features:**
Dagda supports multiple Linux base images:
- Red Hat/CentOS/Fedora
- Debian/Ubuntu
- OpenSUSE
- Alpine

Dagda rests on OWASP dependency check + Retire.js for analyzing multiple dependencies from:
- Java
- Python
- JavaScript
- Ruby
- Php

`Dev-Sec` (https://dev-sec.io/ )

Security + DevOps: Automatic Server Hardening. An excellent resource for automated hardening is a set of open source templates originally developed at Deutsche Telekom. It covers most of the required hardening checks based on multiple standards, which includes Ubuntu Security Features, NSA Guide to Secure Configuration, ArchLinux System Hardening and others.

**Features:**
- Continuous management (this area includes tasks like patch management, attack monitoring, and fixing known vulnerabilities).
- Patch management.
- Attack monitoring (hardening includes a small section of compliance monitoring).
- Vulnerability fixes.

### Operations Stage
`OWASP ZAP` (https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project )

The OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers.

**Features:**
- Automated Penetration Testing to Continuous Integration Pipelines.
- Automated Scanner
- Brute Force Scanner
- Web Sockets
- REST API

`OpenVAS` (http://openvas.org/)

OpenVAS is a full-featured vulnerability scanner. Its capabilities include unauthenticated testing, authenticated testing, various high level and low level Internet and industrial protocols, performance tuning for large-scale scans and a powerful internal programming language to implement any type of vulnerability test.

`CCAT` (https://github.com/RhinoSecurityLabs/ccat)

Cloud Container Attack Tool (CCAT) is a tool for testing security of container environments.

`Spaghetti` (https://github.com/cyberheartmi9/Spaghetti)

Spaghetti is an Open Source web application scanner, it is designed to find various default and insecure files, configurations, and misconfigurations. Spaghetti is built on python2.7 and can run on any platform which has a Python environment.
