╔══════════════════════════════════════════════════════════════╗
║     🌐  FREE AI CHATBOT - PUBLIC DEPLOYMENT GUIDE           ║
║     Groq API + Railway | 24/7 Online | Kabhi Band Nahi      ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 📁 FILES KI LIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  app.py              → Main server (Flask + Groq)
  templates/index.html → Beautiful Chat UI
  requirements.txt    → Python libraries list
  Procfile            → Railway ko batata hai kaise start kare
  railway.json        → Railway config
  README.txt          → Yeh file

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🚀 DEPLOYMENT STEPS (EK BAAR KARO - HO GAYA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

══════════════════════════════════════
 STEP 1: GROQ API KEY Lो (FREE)
══════════════════════════════════════

  1. Browser mein jao: https://console.groq.com
  2. "Sign Up" karo (FREE - koi card nahi chahiye)
  3. Login ke baad: "API Keys" section mein jao
  4. "Create API Key" click karo
  5. Key copy karo → aisi dikhegi: gsk_xxxxxxxxxxxxxxxxxxxx
  6. Is key ko save karo (baad mein chahiye)

══════════════════════════════════════
 STEP 2: GITHUB PE UPLOAD KARO
══════════════════════════════════════

  1. https://github.com pe account banao (free)
  2. "New Repository" click karo
  3. Name do: "free-ai-chatbot"
  4. Public rakho
  5. "Create Repository" click karo
  6. "uploading an existing file" click karo
  7. Saari files drag & drop karo:
       - app.py
       - requirements.txt
       - Procfile
       - railway.json
       - templates/ folder (index.html ke saath)
  8. "Commit changes" click karo

══════════════════════════════════════
 STEP 3: RAILWAY PE DEPLOY KARO (FREE)
══════════════════════════════════════

  1. https://railway.app jao
  2. "Start a New Project" click karo
  3. "Deploy from GitHub repo" choose karo
  4. GitHub se connect karo
  5. Tumhara "free-ai-chatbot" repo select karo
  6. Deploy shuru ho jayega...

  ⚙️  Ab GROQ_API_KEY add karo:
  7. Railway dashboard mein project click karo
  8. "Variables" tab click karo
  9. "Add Variable" click karo:
       Name:  GROQ_API_KEY
       Value: [tumhari groq key yahan paste karo]
  10. Save karo → Auto redeploy hoga

  11. "Settings" → "Domains" mein free URL milega:
       Jaise: https://free-ai-chatbot.up.railway.app

  ✅ DONE! Link share karo duniya ke saath!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 💰 COST - KITNA LAGEGA?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Groq API:   FREE (14,400 requests/day free tier)
  Railway:    FREE ($5 credit/month - kaafi hai)
  GitHub:     FREE
  Domain URL: FREE (.up.railway.app)

  TOTAL = ₹0 (Zero Rupees!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ✅ FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✔ 24/7 Online - Kabhi band nahi hoga
  ✔ 100% Free - Koi payment nahi
  ✔ No Login - Koi account nahi chahiye users ko
  ✔ Hindi + English support
  ✔ 4 AI Models - Llama, Mixtral, Gemma, aur zyada
  ✔ Streaming Response - Real-time typing effect
  ✔ Beautiful Dark UI
  ✔ Mobile Friendly
  ✔ Unlimited users ek saath

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ❌ PROBLEMS & SOLUTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Problem: "Application Error" on Railway
  Fix: Variables mein GROQ_API_KEY sahi se add karo

  Problem: "Rate limit exceeded"
  Fix: Groq free tier mein daily limit hai, kal try karo
       Ya Groq pe paid plan lo ($5/month)

  Problem: Deploy nahi ho raha
  Fix: Check karo requirements.txt sahi hai
       Railway logs mein error dekho

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 🔗 IMPORTANT LINKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Groq Console:   https://console.groq.com
  Railway:        https://railway.app
  GitHub:         https://github.com

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
