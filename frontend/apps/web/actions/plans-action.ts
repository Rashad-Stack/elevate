'use server'

import { getApiClient } from '@/lib/api'
import { ApiError, type PaginatedPlanList } from '@frontend/types/api'

export async function getPlansAction(page?: number): Promise<PaginatedPlanList | null> {
  try {
    const apiClient = await getApiClient()

    const response = await apiClient.plans.plansList(page)

    console.log("🚀 ~ plans-action.ts:12 ~ getPlansAction ~ response:", response);


    return response
  } catch (error) {
    console.error('Failed to fetch plans:', error)
    if (error instanceof ApiError) {
      console.error('API Error:', error.body)
    }
    return null
  }
}