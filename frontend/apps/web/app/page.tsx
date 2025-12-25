import { getPlansAction } from "@/actions";
import { ContentConsistency } from "@/components/landing/content-consistency";
import { ContentSection } from "@/components/landing/content-section";
import { CreatorsShowcase } from "@/components/landing/creators-showcase";
import { CTASection } from "@/components/landing/cta-section";
import { FAQ } from "@/components/landing/faq";
import { FeaturesStack } from "@/components/landing/features-stack";
import { FloatingUsernameClaim } from "@/components/landing/floating-username-claim";
import { Footer } from "@/components/landing/footer";
import { Hero } from "@/components/landing/hero";
import { HowItWorks } from "@/components/landing/how-it-works";
import { Navbar } from "@/components/landing/navbar";
import { PricingPlans } from "@/components/landing/pricing-plans";
import { Testimonials } from "@/components/landing/testimonials";

export default async function Home() {
  // redirect("https://start.elevate.social");
  // Fetch plans data on the server
  const plansData = await getPlansAction();
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <Hero />
      <CreatorsShowcase />
      <ContentConsistency />
      <FeaturesStack />
      <PricingPlans plansData={plansData} />
      <Testimonials />
      <ContentSection />
      <HowItWorks />
      <CTASection />
      <FAQ />
      <Footer />
      <FloatingUsernameClaim />
    </div>
  );
}
