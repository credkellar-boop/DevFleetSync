-- Core User Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    community_id VARCHAR(16) UNIQUE NOT NULL, -- Your generated CID
    platform_id VARCHAR(64),                  -- e.g., Discord ID, Telegram handle
    reputation_score INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Reputation Ledger for "Building Credit"
CREATE TABLE reputation (
    user_id UUID REFERENCES users(id),
    action_type VARCHAR(20), -- 'like', 'course_complete', 'referral'
    points INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Payment & Transaction Records
CREATE TABLE transactions (
    tx_id VARCHAR(128) PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    amount DECIMAL(18, 8),
    currency VARCHAR(10), -- 'USD', 'ETH', 'BUL'
    status VARCHAR(20)    -- 'pending', 'confirmed'
);
