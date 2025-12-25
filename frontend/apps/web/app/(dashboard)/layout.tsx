import { DashboardLayout } from "@/components/dashboard/dashboard-layout";
import { authOptions } from "@/lib/auth";
import { getServerSession } from "next-auth";
import { redirect } from "next/navigation";

export default async function DashboardLayoutWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  const session = await getServerSession(authOptions);

  console.log(
    "🚀 ~ layout.tsx:13 ~ DashboardLayoutWrapper ~ session:",
    session
  );

  if (session === null) {
    return redirect("/");
  }

  return <DashboardLayout>{children}</DashboardLayout>;
}
