try {
        // 🛡️ Ab direct Groq nahi, tumhara Railway backend call ho raha hai
        const response = await fetch('https://grateful-freedom-production.up.railway.app/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: 'llama-3.3-70b-versatile',
            messages: [
              {
                role: 'system',
                content: `You are MK-AI, a smart personal AI assistant made by Mushab Khan.
                Strict Language Rules:
                1. Detect the user's intent and language precisely.
                2. If the user greets or talks in formal/standard English, respond ONLY in professional English.
                3. If the user uses Hinglish, respond in Hinglish.
                4. Creator: Mushab Khan only.`
              },
              ...messages.slice(1), // Welcome message ko chhod kar baki history
              userMsg // User ka naya message
            ],
            max_tokens: 1024,
            temperature: 0.7
          })
        });

        if (!response.ok) throw new Error('Server Error');

        const data = await response.json();
        
        // 🚨 Groq se aaya hua response check karo
        if (data.choices && data.choices[0]) {
          const reply = data.choices[0].message.content;
          setMessages(prev => [...prev, { role: 'assistant', content: reply }]);
          success = true; // Loop todne ke liye
        } else {
          throw new Error('Invalid Response Format');
        }

      }
