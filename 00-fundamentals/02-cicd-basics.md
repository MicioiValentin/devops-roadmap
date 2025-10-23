02 – CI/CD Basics

What CI/CD Means
**CI/CD** stands for **Continuous Integration** and **Continuous Delivery (or Deployment)**.

- **Continuous Integration (CI):**  
  Developers frequently merge their code changes into a shared branch.  
  Each commit triggers an automated build and test process to detect issues early.

- **Continuous Delivery / Deployment (CD):**  
  Once code passes all tests, it’s automatically deployed to a staging or production environment with minimal manual intervention.

Together, CI/CD ensures software is always in a **deployable state** and updates reach users **quickly and safely**

What a Pipeline Does

A **pipeline** is a series of automated steps that handle the process from code commit to deployment.  
It typically includes:
1. **Build:** compile or package the application.  
2. **Test:** run automated unit/integration tests.  
3. **Deploy:** push to staging or production.  
4. **Monitor:** verify deployment success.

Each stage provides feedback and can stop the process if something fails.

Azure Pipelines vs GitHub Actions

| Feature | **Azure Pipelines** | **GitHub Actions** |


| **Integration** | Part of Azure DevOps ecosystem | Built directly into GitHub |
| **Configuration** | YAML or Classic UI | YAML in `.github/workflows` |
| **Supported Repos** | Any Git repo (GitHub, GitLab, Bitbucket) | Primarily GitHub |
| **Agents** | Microsoft-hosted or self-hosted | GitHub-hosted or self-hosted |
| **Best For** | Enterprises using Azure DevOps projects | Developers already using GitHub |
| **Use Case Example** | Large teams with separate build/release pipelines | Individual or OSS projects needing fast automation |
