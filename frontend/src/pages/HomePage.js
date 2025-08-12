// use client
import React, { useState, useEffect } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import {
  Button
} from "../components/ui/Button";
import {
  Card,
  CardContent
} from "../components/ui/Card";
import { Badge } from "../components/ui/Badge";
import {
  Brain,
  FileText,
  Calendar,
  Shield,
  Users,
  ArrowRight,
  CheckCircle,
  Star,
  Sparkles,
  Zap,
  Award,
  TrendingUp,
  Video,
  Globe,
  Mic,
  UserCheck
} from "lucide-react";
import { Navbar } from "../components/Navbar";
import { Footer } from "../components/Footer";
import { Link } from "react-router-dom";

// Theme colors
const THEME_COLOR = "#a78bfa"; // purple
const THEME_COLOR_LIGHT = "rgba(167,139,250,0.5)";

const stats = [
  { icon: <Users size={32} />, label: "Users", value: "12K+" },
  { icon: <TrendingUp size={32} />, label: "Growth", value: "320%" },
  { icon: <Award size={32} />, label: "Awards", value: "8" },
  { icon: <Star size={32} />, label: "Rating", value: "4.9/5" }
];

const features = [
  {
    icon: <Brain size={28} />,
    title: "AI-Powered Insights",
    desc: "Unlock smarter decisions with advanced analytics.",
    demo: "Try AI Demo"
  },
  {
    icon: <FileText size={28} />,
    title: "Document Automation",
    desc: "Automate workflows and reduce manual effort.",
    demo: "See Automation"
  },
  {
    icon: <Shield size={28} />,
    title: "Secure Storage",
    desc: "Your data is encrypted and protected.",
    demo: "View Security"
  },
  {
    icon: <Sparkles size={28} />,
    title: "Smart Search",
    desc: "Find anything instantly with semantic search.",
    demo: "Test Search"
  },
  {
    icon: <Zap size={28} />,
    title: "Real-Time Collaboration",
    desc: "Work together seamlessly, anywhere.",
    demo: "Collaborate Now"
  },
  {
    icon: <Calendar size={28} />,
    title: "Integrated Calendar",
    desc: "Never miss a deadline or meeting.",
    demo: "See Calendar"
  }
];

const marketplaceBenefits = [
  "Instant access to top experts",
  "Transparent bidding system",
  "Verified service providers",
  "Secure payments",
  "Live project tracking"
];

const marketplaceDemo = [
  { name: "Expert Bid", price: "$120", status: "Active" },
  { name: "Consultation", price: "$80", status: "Pending" }
];

const labs = [
  { icon: <Video size={24} />, title: "Docs Summarizer", desc: "Summarize documents instantly.", status: "Live" },
  { icon: <Globe size={24} />, title: "Global Translator", desc: "Translate documents in 50+ languages.", status: "Beta" },
  { icon: <Mic size={24} />, title: "Voice Notes", desc: "Transcribe and organize voice notes.", status: "Coming Soon" },
  { icon: <UserCheck size={24} />, title: "Identity Verifier", desc: "Verify users securely.", status: "Live" },
  { icon: <Star size={24} />, title: "Reputation Engine", desc: "Track and build trust.", status: "Beta" },
  { icon: <Sparkles size={24} />, title: "Smart Templates", desc: "Auto-generate docs.", status: "Coming Soon" }
];

const testimonials = [
  {
    stars: 5,
    quote: "Documind transformed our workflow. The AI features are game-changing!",
    name: "Priya Sharma",
    role: "Operations Lead",
    img: "https://randomuser.me/api/portraits/women/44.jpg"
  },
  {
    stars: 5,
    quote: "Secure, fast, and reliable. Highly recommended for any team.",
    name: "Rahul Verma",
    role: "Product Manager",
    img: "https://randomuser.me/api/portraits/men/32.jpg"
  },
  {
    stars: 4,
    quote: "The marketplace and labs are unique. Excited for future updates!",
    name: "Ayesha Khan",
    role: "Innovation Strategist",
    img: "https://randomuser.me/api/portraits/women/68.jpg"
  }
];

const plans = [
  {
    name: "Starter",
    price: "$0",
    desc: "Basic features for individuals.",
    features: ["AI Insights", "Secure Storage", "Smart Search"],
    popular: false
  },
  {
    name: "Pro",
    price: "$19/mo",
    desc: "Advanced tools for professionals.",
    features: ["All Starter features", "Document Automation", "Collaboration", "Integrated Calendar"],
    popular: true
  },
  {
    name: "Business",
    price: "$49/mo",
    desc: "Full suite for teams and businesses.",
    features: ["All Pro features", "Marketplace Access", "Labs", "Priority Support"],
    popular: false
  },
  {
    name: "Enterprise",
    price: "Contact Us",
    desc: "Custom solutions for large organizations.",
    features: ["All Business features", "Custom Integrations", "Dedicated Manager"],
    popular: false
  }
];

// Mouse tracking for animated background
function useMousePosition() {
  const [pos, setPos] = useState({ x: window.innerWidth / 2, y: window.innerHeight / 2 });
  useEffect(() => {
    const handler = (e) => setPos({ x: e.clientX, y: e.clientY });
    window.addEventListener("mousemove", handler);
    return () => window.removeEventListener("mousemove", handler);
  }, []);
  return pos;
}

export default function HomePage() {
  const mouse = useMousePosition();
  const { scrollY } = useScroll();
  const heroY = useTransform(scrollY, [0, 300], [0, -80]);
  const heroOpacity = useTransform(scrollY, [0, 300], [1, 0]);

  // Pulse animation for static circles
  const [pulse, setPulse] = useState(1);
  useEffect(() => {
    const interval = setInterval(() => {
      setPulse((p) => (p === 1 ? 1.2 : 1));
    }, 1200);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-black via-gray-900 to-[#1e1b4b] relative overflow-x-hidden">
      <Navbar brand="Documind" />
      {/* Animated Background */}
      <div className="fixed inset-0 pointer-events-none z-0">
        {/* Mouse-following circle */}
        <motion.div
          style={{
            left: mouse.x - 150,
            top: mouse.y - 150,
            background: THEME_COLOR_LIGHT,
            scale: pulse
          }}
          className="absolute w-[300px] h-[300px] rounded-full blur-3xl"
        />
        {/* Static pulsing circles */}
        <motion.div
          animate={{ scale: pulse }}
          className="absolute top-24 left-1/4 w-[220px] h-[220px] rounded-full blur-2xl"
          style={{ background: THEME_COLOR_LIGHT }}
        />
        <motion.div
          animate={{ scale: 1.1 - (pulse - 1) }}
          className="absolute bottom-32 right-1/4 w-[180px] h-[180px] rounded-full blur-2xl"
          style={{ background: THEME_COLOR_LIGHT }}
        />
      </div>
      {/* Hero Section */}
      <motion.section
        style={{ y: heroY, opacity: heroOpacity }}
        className="relative z-10 flex flex-col items-center justify-center pt-32 pb-20 px-6 lg:px-8 text-center"
      >
        <Badge className="mb-4 bg-gradient-to-r from-purple-500 to-indigo-500 text-white border-none shadow-lg">
          Welcome to Documind
        </Badge>
        <motion.h1
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="text-5xl md:text-7xl font-extrabold mb-6 bg-gradient-to-r from-purple-400 via-purple-600 to-indigo-400 text-transparent bg-clip-text"
        >
          Supercharge Your Documents
        </motion.h1>
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.7 }}
          className="max-w-2xl mx-auto text-lg md:text-xl text-gray-300 mb-8"
        >
          AI-powered platform for smarter, faster, and secure document management.
        </motion.p>
        <div className="flex flex-col md:flex-row gap-4 justify-center mb-10">
          <Button className="bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-lg hover:scale-105 transition" asChild>
            <Link to="/auth/signup">
              Get Started
            </Link>
          </Button>
          <Button variant="outline" className="border-purple-400 text-purple-300 hover:bg-purple-900/30 hover:scale-105 transition" asChild>
            <Link to="/learn-more">
              Learn More
            </Link>
          </Button>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mt-8">
          {stats.map((stat, i) => (
            <Card key={i} className="bg-black/60 border-purple-900/30 text-white shadow-lg">
              <CardContent className="flex flex-col items-center py-6">
                <div className="mb-2">{stat.icon}</div>
                <div className="text-2xl font-bold">{stat.value}</div>
                <div className="text-sm text-purple-300">{stat.label}</div>
              </CardContent>
            </Card>
          ))}
        </div>
      </motion.section>
      {/* Features Section */}
      <section id="features" className="relative z-10 py-20 px-6 lg:px-8">
        <h2 className="text-3xl md:text-4xl font-bold text-white mb-10 text-center">
          Powerful Features
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((f, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
            >
              <Card className="bg-gradient-to-br from-black via-gray-900 to-purple-900 border-purple-900/30 text-white shadow-lg hover:scale-105 transition">
                <CardContent className="flex flex-col items-center py-8">
                  <div className="mb-4 p-4 rounded-full bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-lg">
                    {f.icon}
                  </div>
                  <div className="text-xl font-semibold mb-2">{f.title}</div>
                  <div className="text-gray-300 mb-2">{f.desc}</div>
                  <Badge className="bg-purple-700/80 text-white">{f.demo}</Badge>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </section>
      {/* Marketplace Section */}
      <section id="marketplace" className="relative z-10 py-20 px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
              Service Marketplace
            </h2>
            <p className="text-gray-300 mb-6">
              Connect with top experts and providers for all your document needs.
            </p>
            <ul className="mb-6 space-y-2">
              {marketplaceBenefits.map((b, i) => (
                <li key={i} className="flex items-center text-purple-300">
                  <CheckCircle className="mr-2 text-purple-400" size={18} />
                  {b}
                </li>
              ))}
            </ul>
            <div className="flex gap-4">
              <Button className="bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-lg" asChild>
                <Link to="/marketplace">Explore Marketplace</Link>
              </Button>
              <Button variant="outline" className="border-purple-400 text-purple-300 hover:bg-purple-900/30" asChild>
                <Link to="/auth/signup">Join Now</Link>
              </Button>
            </div>
          </div>
          <Card className="bg-black/60 border-purple-900/30 text-white shadow-lg">
            <CardContent className="py-8">
              <h3 className="text-xl font-bold mb-4">Live Bids</h3>
              <ul>
                {marketplaceDemo.map((item, i) => (
                  <li key={i} className="flex justify-between items-center mb-2">
                    <span>{item.name}</span>
                    <Badge className="bg-purple-700/80 text-white">{item.price}</Badge>
                    <Badge className="bg-purple-900/80 text-white">{item.status}</Badge>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        </div>
      </section>
      {/* Labs Section */}
      <section id="labs" className="relative z-10 py-20 px-6 lg:px-8">
        <h2 className="text-3xl md:text-4xl font-bold text-white mb-10 text-center">
          Innovation Labs
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {labs.map((lab, i) => (
            <Card key={i} className="bg-gradient-to-br from-black via-gray-900 to-purple-900 border-purple-900/30 text-white shadow-lg">
              <CardContent className="flex flex-col items-center py-8">
                <div className="mb-4 p-3 rounded-full bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-lg">
                  {lab.icon}
                </div>
                <div className="text-lg font-semibold mb-2">{lab.title}</div>
                <div className="text-gray-300 mb-2">{lab.desc}</div>
                <Badge
                  className={
                    lab.status === "Live"
                      ? "bg-green-600/80 text-white"
                      : lab.status === "Beta"
                      ? "bg-yellow-500/80 text-white"
                      : "bg-gray-600/80 text-white"
                  }
                >
                  {lab.status}
                </Badge>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>
      {/* Testimonials Section */}
      <section id="testimonials" className="relative z-10 py-20 px-6 lg:px-8">
        <h2 className="text-3xl md:text-4xl font-bold text-white mb-10 text-center">
          What Our Users Say
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {testimonials.map((t, i) => (
            <Card key={i} className="bg-black/60 border-purple-900/30 text-white shadow-lg">
              <CardContent className="flex flex-col items-center py-8">
                <div className="flex mb-2">
                  {[...Array(t.stars)].map((_, idx) => (
                    <Star key={idx} className="text-yellow-400" size={20} />
                  ))}
                </div>
                <p className="text-lg italic mb-4 text-gray-200">"{t.quote}"</p>
                <img src={t.img} alt={t.name} className="w-14 h-14 rounded-full mb-2 object-cover" />
                <div className="font-semibold">{t.name}</div>
                <div className="text-purple-300 text-sm">{t.role}</div>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>
      {/* Pricing Section */}
      <section id="pricing" className="relative z-10 py-20 px-6 lg:px-8">
        <h2 className="text-3xl md:text-4xl font-bold text-white mb-10 text-center">
          Pricing Plans
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {plans.map((plan, i) => (
            <Card
              key={i}
              className={`bg-gradient-to-br from-black via-gray-900 to-purple-900 border-purple-900/30 text-white shadow-lg relative ${
                plan.popular ? "border-2 border-purple-400" : ""
              }`}
            >
              <CardContent className="flex flex-col items-center py-8">
                {plan.popular && (
                  <Badge className="absolute top-4 right-4 bg-purple-500 text-white shadow-lg">
                    Popular
                  </Badge>
                )}
                <div className="text-2xl font-bold mb-2">{plan.name}</div>
                <div className="text-xl mb-2">{plan.price}</div>
                <div className="text-gray-300 mb-4">{plan.desc}</div>
                <ul className="mb-6 space-y-2">
                  {plan.features.map((f, idx) => (
                    <li key={idx} className="flex items-center text-purple-300">
                      <CheckCircle className="mr-2 text-purple-400" size={18} />
                      {f}
                    </li>
                  ))}
                </ul>
                <Button
                  className="bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-lg w-full"
                  asChild
                >
                  <Link to="/auth/signup">Choose Plan</Link>
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>
      {/* CTA Section */}
      <section className="relative z-10 py-20 px-6 lg:px-8 flex justify-center">
        <Card className="bg-gradient-to-br from-black via-gray-900 to-purple-900 border-purple-900/30 text-white shadow-2xl max-w-2xl w-full">
          <CardContent className="flex flex-col items-center py-12">
            <h3 className="text-2xl md:text-3xl font-bold mb-4 text-center">
              Ready to transform your document workflow?
            </h3>
            <p className="text-gray-300 mb-8 text-center">
              Join Documind today and experience the future of document management.
            </p>
            <div className="flex gap-4">
              <Button className="bg-gradient-to-r from-purple-500 to-indigo-500 text-white shadow-lg" asChild>
                <Link to="/auth/signup">Get Started</Link>
              </Button>
              <Button variant="outline" className="border-purple-400 text-purple-300 hover:bg-purple-900/30" asChild>
                <Link to="/learn-more">Learn More</Link>
              </Button>
            </div>
          </CardContent>
        </Card>
      </section>
      <Footer brand="Documind" />
    </div>
  );
}