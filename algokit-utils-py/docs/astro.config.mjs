// @ts-check
import starlight from "@astrojs/starlight";
import { defineConfig } from "astro/config";
import remarkGithubAlerts from "remark-github-alerts";
import sidebar from "./sidebar.config.json";
import remarkRebaseLinks from "./plugins/remark-rebase-links.mjs";

// The combined GitHub Pages deployment sets DOCS_SITE and DOCS_BASE to serve this site under a sub-path.
const base = process.env.DOCS_BASE || "/algokit-utils-py/";

// https://astro.build/config
export default defineConfig({
  site: process.env.DOCS_SITE || "https://algorandfoundation.github.io",
  base,
  trailingSlash: "always",
  markdown: {
    remarkPlugins: [remarkGithubAlerts, [remarkRebaseLinks, { from: "/algokit-utils-py/", to: base }]],
  },
  integrations: [
    starlight({
      title: "AlgoKit Utils Python",
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 4 },
      customCss: [
        "./src/styles/api-reference.css",
        "remark-github-alerts/styles/github-colors-light.css",
        "remark-github-alerts/styles/github-colors-dark-media.css",
        "remark-github-alerts/styles/github-base.css",
      ],
      social: [
        {
          icon: "github",
          label: "GitHub",
          href: "https://github.com/algorandfoundation/algokit-py/tree/main/algokit-utils-py",
        },
        {
          icon: "discord",
          label: "Discord",
          href: "https://discord.gg/algorand",
        },
      ],
      sidebar,
    }),
  ],
});
