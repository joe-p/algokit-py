// @ts-check

/**
 * Remark plugin that rewrites internal links and images written against a
 * fixed base path to the configured Astro `base`.
 *
 * The hand-written docs link to pages with absolute paths such as
 * `/algokit-utils-py/tutorials/quick-start/`, but the site can be deployed
 * under a different base (e.g. `/algokit-py/utils/` on the combined GitHub
 * Pages site).
 *
 * @param {{ from: string, to: string }} options
 */
export default function remarkRebaseLinks({ from, to }) {
  /** @param {any} node */
  const visit = (node) => {
    if ((node.type === "link" || node.type === "image" || node.type === "definition") && node.url.startsWith(from)) {
      node.url = to + node.url.slice(from.length);
    }
    node.children?.forEach(visit);
  };
  /** @param {any} tree */
  return (tree) => {
    if (from !== to) visit(tree);
  };
}
