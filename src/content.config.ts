import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const guides = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guides' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().default(50),
    updated: z.string().optional(),
  }),
});
const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    category: z.enum(['Jobs', 'Syllabus', 'Results', 'Test dates', 'Updates', 'Preparation']),
    post: z.string().optional(),
  }),
});
export const collections = { guides, news };
