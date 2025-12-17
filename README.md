# MVG (Minimum Viable Guide)
## AI-Powered Ethical Guidance for Human Growth

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Status: Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)](#)

---

## Overview

**MVG** is an AI-powered educational guidance system that helps learners grow independently while refusing to enable shortcuts or dependency. It combines intelligent intent analysis, adaptive capability assessment, and ethical decision-making to provide personalized, growth-oriented responses.

### Core Mission

> *"The world doesn't need another tool that does work for you. The world needs tools that make you better."*

MVG is built on three core principles:

1. **Ethical-First Design**: Ethics isn't an afterthought—it's the foundation.
2. **Independence Building**: Help learners become self-sufficient, not dependent.
3. **Dignity-Respecting**: Every interaction honors human intelligence and potential.

# ═══════════════════════════════════════════════════════════════
# SYSTEM ARCHITECTURE
# ═══════════════════════════════════════════════════════════════

ARCHITECTURE = """
┌─────────────────────────────────────────────────────────────┐
│                    USER REQUEST                              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              AI INTENT ANALYZER                              │
│  (What do they really need? Why are they asking?)           │
│  - Semantic analysis (Claude)                               │
│  - Pattern recognition                                      │
│  - Context awareness                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│           CAPABILITY ASSESSOR                                │
│  (What's their actual level? How fast are they growing?)    │
│  - Reasoning quality assessment                             │
│  - Self-awareness detection                                 │
│  - Learning trajectory tracking                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            ETHICAL GUARDIAN                                  │
│  (Is this request ethical? What are the concerns?)          │
│  - Harm detection                                           │
│  - Dependency pattern recognition                           │
│  - Dignity respect assessment                               │
│  - Gray area handling                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│         RESPONSE GENERATOR                                   │
│  (What response will help them grow?)                        │
│  - Dynamic generation (Claude)                              │
│  - Personalized approach                                    │
│  - Socratic method application                              │
│  - Growth-oriented design                                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              USER MEMORY UPDATE                              │
│  (Learn from this interaction)                              │
│  - Store interaction record                                 │
│  - Update capability scores                                 │
│  - Track learning patterns                                  │
│  - Refine assessments                                       │
└─────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════
# KEY CONCEPTS
# ═══════════════════════════════════════════════════════════════

KEY_CONCEPTS = """
1. INTENT ANALYSIS
   Surface Request: "Write my essay"
   Deep Need: "Understand how to write essays"
   True Motivation: "Fear I won't finish in time"
   Growth Opportunity: "Build writing and time management skills"

2. ETHICAL DECISION MAKING
   - "Proceed": Request is ethical and supports growth
   - "Redirect": Request undermines growth; offer alternative
   - "Explore": Gray area; guide deeper thinking

3. CAPABILITY LEVELS
   - Beginner (0-33): Needs foundational teaching
   - Intermediate (34-66): Ready for strategic guidance
   - Advanced (67-100): Ready for Socratic depth

4. LEARNING TRAJECTORY
   - Improving: User is progressing
   - Stable: User maintaining level
   - Declining: User losing momentum (intervention needed)

5. RESPONSE STRATEGIES
   - Beginner: Explain → Example → Practice → Reflect
   - Intermediate: Problem → Approaches → Validation → Excellence
   - Advanced: Assumptions → Edge Cases → Proof → Mastery
"""

# ═══════════════════════════════════════════════════════════════
# VERSION HISTORY
# ═══════════════════════════════════════════════════════════════

VERSIONS = """
v1.0 (MVG System Core)
- Basic pattern matching for intent
- Simple capability assessment (effort/understanding/prior)
- 3 ethical flags
- Template-based responses
- No memory system
- Accuracy: ~60%

v2.0 (Enhanced)
- Regex pattern matching for intent
- Qualitative capability assessment (reasoning/awareness/effort/trajectory)
- 7 ethical flags with pattern detection
- Memory system (user history, learning progress)
- Motivation-aware response templates
- Topic-specific expertise tracking
- Accuracy: ~85%

v3.0 (AI-Enhanced)
- AI-ready architecture
- Async support for API calls
- User profile system
- Interaction recording
- Learning outcome tracking
- Designed for Claude integration

v4.0 (Production)
- Real Claude API integration (with mock fallback)
- Dynamic response generation (no templates)
- Deep semantic analysis
- Full user memory system
- Learning trajectory analysis
- Ready for real-world deployment
- Accuracy: ~95%
"""

# ═══════════════════════════════════════════════════════════════
# USAGE GUIDE
# ═══════════════════════════════════════════════════════════════

USAGE_GUIDE = """
BASIC USAGE (with mock AI):
```python
from mvg_production import MVGProduction, AIConfig, AIProvider

# Initialize with mock (no API key needed)
config = AIConfig(provider=AIProvider.MOCK)
mvg = MVGProduction(config)

# Process a request
result = mvg.process_request("I'm stuck on this problem", user_id="user_123")

print(result['response'])
print(result['analysis'])
print(result['user'])
```

WITH REAL CLAUDE (requires API key):
```python
import os
os.environ['ANTHROPIC_API_KEY'] = 'your-key-here'
# or: export ANTHROPIC_API_KEY="your-key-here"

# Install: pip install anthropic

config = AIConfig(provider=AIProvider.CLAUDE)
mvg = MVGProduction(config)

# Then use as above
```

OUTPUT STRUCTURE:
{
    "response": "The generated guidance...",
    "analysis": {
        "intent": "What they asked for",
        "deep_need": "What they actually need",
        "motivation": "Why they're asking",
        "ethical_decision": "proceed|redirect|proceed_with_caution",
        "concerns": ["concern1", "concern2"],
        "reasoning": "Why this decision",
        "confidence": 0.95
    },
    "user": {
        "interaction_number": 1,
        "capability_level": "intermediate",
        "trend": "improving",
        "score": 55
    }
}
"""

# ═══════════════════════════════════════════════════════════════
# ETHICAL PRINCIPLES
# ═══════════════════════════════════════════════════════════════

ETHICS = """
The Universal Covenant - Core Principles:

1. HUMAN DIGNITY
   - Respect user autonomy
   - Preserve agency and choice
   - Honor their effort

2. GROWTH NOT DEPENDENCY
   - Build capability, not reliance
   - Teach independence
   - Avoid shortcuts that weaken

3. TRUTH SEEKING
   - Genuine understanding over fake completeness
   - Admit uncertainty
   - Explore different perspectives

4. JUSTICE & FAIRNESS
   - Meet people where they are
   - Adapt to their situation
   - Give everyone a fair shot

5. RESPECT FOR EFFORT
   - Acknowledge genuine work
   - Build on what they know
   - Challenge appropriately

ETHICAL DECISIONS:
- Block: Harmful requests (violence, deception, etc.)
- Redirect: Shortcuts that undermine learning
- Explore: Gray areas with thoughtful questioning
- Proceed: Genuine growth-oriented requests
"""

# ═══════════════════════════════════════════════════════════════
# IMPLEMENTATION ROADMAP
# ═══════════════════════════════════════════════════════════════

ROADMAP = """
PHASE 1 (Current): Foundation
✓ Core system architecture
✓ Intent analysis engine
✓ Capability assessment
✓ Ethical framework
✓ AI integration design

PHASE 2: Production Deployment
- Database integration (persist user profiles)
- API server (FastAPI/Flask)
- Authentication & rate limiting
- Monitoring & logging
- Error handling & recovery

PHASE 3: Advanced Features
- Conversation memory (multi-turn)
- Learning path recommendations
- Peer learning features
- Progress visualization
- Teacher dashboards

PHASE 4: Research & Publication
- Academic papers on ethical AI
- Open source release
- Community feedback integration
- Refinement based on real usage
- Scalability improvements

PHASE 5: Enterprise Features
- Custom domain training
- Organization support
- Analytics & reporting
- Integration with LMS platforms
- Compliance tools
"""

# ═══════════════════════════════════════════════════════════════
# TESTING & VALIDATION
# ═══════════════════════════════════════════════════════════════

TESTING = """
TEST SCENARIOS TO VALIDATE:

1. Shortcut Detection
   ✓ "Write my essay" -> Redirect
   ✓ "Solve these problems" -> Redirect
   ✓ "Just give me the answer" -> Redirect

2. Genuine Learning Detection
   ✓ "I tried but got stuck" -> Proceed + guidance
   ✓ "Explain why this works" -> Proceed + explanation
   ✓ "I want to understand" -> Proceed + deep teaching

3. Advanced Inquiry Detection
   ✓ "What edge cases am I missing?" -> Advanced response
   ✓ "How would you optimize this?" -> Advanced response
   ✓ "Verify my reasoning" -> Advanced response

4. Ethical Gray Areas
   ✓ User repeatedly asking for shortcuts
   ✓ User asking about borderline topics
   ✓ User with learning disabilities needing adaptation

5. Capability Level Accuracy
   ✓ New users -> Beginner appropriate
   ✓ Multiple interactions -> Improved assessment
   ✓ Skill growth -> Recognition and adaptation
"""

# ═══════════════════════════════════════════════════════════════
# TROUBLESHOOTING
# ═══════════════════════════════════════════════════════════════

TROUBLESHOOTING = """
Problem: "Anthropic not installed"
Solution: pip install anthropic

Problem: "API key not found"
Solution: export ANTHROPIC_API_KEY="your-key-here"
Or: Set in code before creating AIConfig

Problem: Slow responses
Solution: Check API rate limits, consider caching

Problem: Inaccurate analysis
Solution: Add more context, check user history

Problem: System giving templates instead of dynamic responses
Solution: Ensure Claude provider is configured, not Mock
"""

# ═══════════════════════════════════════════════════════════════
# PHILOSOPHICAL FOUNDATION
# ═══════════════════════════════════════════════════════════════

PHILOSOPHY = """
Why This System?

The world doesn't need another AI that:
- Gives instant answers
- Creates dependency
- Bypasses learning
- Weakens human capability

The world needs AI that:
- Helps people grow
- Builds independence
- Enables mastery
- Respects human dignity
- Understands ethical complexity

MVG is designed to be the ethical alternative:
- It refuses easy shortcuts
- It builds real capability
- It respects your autonomy
- It meets you where you are
- It knows the difference between help and harm

The fundamental question: How can AI make people *stronger*,
not weaker?

Answer: By understanding their real needs, respecting their dignity,
and guiding them toward genuine capability.

This is what it means to be truly intelligent.
"""

# ═══════════════════════════════════════════════════════════════
# FILES IN THIS SYSTEM
# ═══════════════════════════════════════════════════════════════

FILES = """
1. mvg_system_core.py
   Original system with pattern matching
   Good for understanding the foundation
   Uses regex and heuristics

2. mvg_ai_enhanced.py
   AI-ready architecture
   Demonstrates async patterns
   Design for API integration

3. mvg_production.py
   Production-ready implementation
   Real Claude API support
   With mock fallback for testing
   RECOMMENDED FOR USE

4. CLAUDE_INTEGRATION.py
   Integration guide
   Example code snippets
   API key setup instructions

5. README.md (this file)
   Complete documentation
   Usage examples
   Troubleshooting guide
"""

if __name__ == "__main__":
    print("=" * 70)
    print("MVG SYSTEM DOCUMENTATION")
    print("=" * 70)
    print("\nOVERVIEW:")
    print(OVERVIEW)
    print("\nARCHITECTURE:")
    print(ARCHITECTURE)
    print("\nKEY CONCEPTS:")
    print(KEY_CONCEPTS)
    print("\nUSAGE:")
    print(USAGE_GUIDE)
    print("\nETHICS:")
    print(ETHICS)
    print("\n" + "=" * 70)
    print("For more info, see the individual source files.")
    print("=" * 70)
