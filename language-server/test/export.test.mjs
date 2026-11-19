import assert from 'node:assert/strict';
import { test } from 'node:test';
import { previewMarkdown } from '../node_modules/@markup-carve/carve-lsp/dist/preview.js';

test('the pinned server exports Carve 0.2 as Markdown', () => {
  assert.equal(previewMarkdown('= Title\n\n/em/ and *strong*\n'), '# Title\n\n*em* and **strong**\n');
});
