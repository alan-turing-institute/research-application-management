
# The RAM team's public-facing website

The RAM team's public-facing website lives in here. It's made with [Zeon Studio](https://zeon.studio)'s [Hugo + Tailwind CSS Starter and Boilerplate](https://hugoplate.netlify.app).

## Run locally

In order to run the site locally, you should be able to go through the following steps:

1. Install all the dependencies using the following command.

   ```bash
   npm install
   ```

2. Run the following command to start the development server.

   ```bash
   npm run dev
   ```

## Customization

- You can change the site title, base URL, language, theme, plugins, and more from the `hugo.toml` file.
- You can customize all the parameters from the `config/_default/params.toml` file. This includes the logo, favicon, search, SEO metadata, and more.
- You can change the colors and fonts from the `data/theme.json` file. This includes the primary color, secondary color, font family, and font size.
- You can add social links from the `data/social.json` file. Add your social links here, and they will automatically be displayed on the site.

## Update Theme

If you want to update the theme, then you can use the following command, which will update the theme to the latest version:

```bash
npm run update-theme
```

There are also a lot of modules added in this template. You can update all the modules using the following command:

```bash
npm run update-modules
```
