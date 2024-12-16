import client from '$lib/clients/client';
import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const { data, error, response } = await client.GET('/api/v1/quiblets/{name}/', {
    params: {
      path: { name: params.name }
    }
  });

  if (response.ok && data) {
    if (data.name !== params.name) {
      redirect(307, `/q/${data.name}`);
    }
    return { quiblet: data };
  } else if (error) {
    redirect(309, '/');
  }
};
