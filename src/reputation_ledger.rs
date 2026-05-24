use sqlx::PgPool;

pub async fn update_user_reputation(pool: &PgPool, user_id: &str, points: i32) -> Result<(), sqlx::Error> {
    // Upsert reputation points based on community engagement
    sqlx::query!(
        "INSERT INTO reputation (user_id, total_points) 
         VALUES ($1, $2) 
         ON CONFLICT (user_id) 
         DO UPDATE SET total_points = reputation.total_points + $2",
        user_id,
        points
    )
    .execute(pool)
    .await?;
    
    Ok(())
}
