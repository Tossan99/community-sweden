# community-sweden

![Community Sweden](documentation_media/community_sweden.jpg)

We're thrilled to introduce you to our community-driven website, designed to support and enhance your journey through the Code Institute course. As a community passionate about learning and collaboration, we've created this platform to empower everyone to participate in coding and gain a deeper understanding of Django.

## Table of Content

## Conventions to Follow

### Double or Single Quotation Marks
- We use `double quotation` marks for the outer quotes and `single quotation` marks for quotes within quotes. Ex: let string = "This is a 'string' with a quote"

### Spacing
- We use `4 spaces` for `indentation`.

### Urls
- The best `URLs` are clearly named and should almost be possible to be guessed by users. So, choose a structure that makes sense for this project. The About Us page may live at the `about/` `URL`, whereas logging into your site may live at `accounts/login/`.
- Although it may be tempting, it is best not to give your `URLs` the same name as your `view function` or vice versa. So, our `blog/` `URL` would not call a `view function` named blog.

### Branch / Fork

Before you start working on this project, you must create your own branch by clicking "branches" and then the green "new branch" button. Then you can open the branch in your IDE.
We will use branches rather than forks, unless there is a need to deploy an additional live version.

It's important that you only push changes to your own branch so that nobody overwrites the main repository. From there, you can migrate your changes to the main branch by making a pull request to merge your branch onto main. 

<details>
<summary>Branching instructions</summary>

1. Click "new branch"
2. Copy the URL or SSL key 
3. Open your IDE
4. Using the command palette, type in 'Git: Clone'
5. Paste the URL or SSL key and press Enter
6. Choose where to place your local repository
7. In your terminal, type in ```pip3 install -r requirements.txt``` to install all dependencies

Now you're good to go.
</details>

### Merging and Pull requests

In order to merge your changes onto the main repository and keep everything in sync, you have to do a pull request. This will compare the differences between your branch and the main branch. If everything is compatible, you can automatically merge it. If not, someone must resolve the conflicts and approve the pull. Don't worry, all of this is easy and straightforward.

Also, it's important to know the right order of staging, committing, pulling and pushing. Pushing before pulling can cause problems on github. Conversely, pulling before you will overwrite your local code with the code from the github repo.
Again, don't worry, you will quickly get the hang of this, and there will be more details below.

__Useful Git commands__

<details>
<summary>Merge/pull instructions</summary>

- ```git add .``` to stage all your changes
- ```git commit -m "your message here"``` to commit your changes with a message
- ```git pull origin main``` to pull the code from the main repo. If it asks you about rebasing the code, you can use ```git config pull.rebase true```
- ```git push``` to push your code onto your local branch

</details>

## env.py
- DM one of our members on slack to get access to the `env.py` file and its keys.
- You will need these keys to work on the project, just like you need a key to start a car.

## Setting Up a New App
- Follow this short guide to set up your own `app` in our community project:
