"use client";

import { Metadata } from "next";
import { Icons } from "@/components/icons";

import { Button } from "@/components/ui/button";
import { MainNav } from "@/components/main-nav";
import Link from "next/link";
import TextAnimation from "@/components/text-animation";
import Footer from "./Footer";
import Search from "./Search";

export default function HomePage() {
  const TextArray = ["Python", "JavaScript", "GitHub", "PyPI", "JavaScript"];

  return (
    <main className="h-[65vh] w-full justify-center items-center flex px-4 flex-col ">
      <div className="hidden flex-col md:flex md-10">
        <div className="flex h-16 flex-end px-4 w-screen">
          <MainNav className="mx-6" />
          <div className="ml-auto flex items-center space-x-4">
            <Button variant="outline" asChild>
              <Link href="https://github.com/amal-thundiyil/vigil">
                <Icons.gitHub className="h-5 w-5" />
              </Link>
            </Button>
            <Button>Sign In</Button>
          </div>
        </div>
      </div>
      <div className="scroll-m-20 text-2xl sm:text-3xl md:text-4xl font-extrabold tracking-normal lg:text-5xl text-center space-y-3 justify-center mt-40">
        Software Supply Chain Protection {<br />}
        <span className="flex gap-2">
          for
          <TextAnimation
            className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl"
            words={TextArray}
          />
        </span>
      </div>
      <Search />
      <Footer />
    </main>
  );
}